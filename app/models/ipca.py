from datetime import datetime

import pandas as pd
from pathlib import Path

from dateutil.relativedelta import relativedelta


class IpcaModel(object):

    def __init__(self):
        self.arquivo = './app/models/ipca.xlsx'
        self.df = None

    @property
    def valores(self):
        """
        Para calcular é preciso calcular o fator 1 + i, utilizando a parcela “i” como taxa unitária
        (que é dividir a variação percentual por 100 antes de somar 1), e multiplicar essa quantidade pela
        quantidade de períodos que quiser acumular.
        Fonte: https://notaalta.espm.br/fala-professor/e-esse-ipca-acumulado-em-968-como-se-calcula-isso/
        :return: pd.dataframe
        """
        df = pd.read_excel(self.arquivo)
        df.sort_values(by=['data'], inplace=True)
        df['i'] = (df['valor'] / 100) + 1
        df['acumulado'] = df['i'].cumprod()
        df['porcentagem'] = ((df['acumulado'] - 1) * 100)
        df['porcentagem'] = df['porcentagem'].round(2)
        df_retorno = df[['data', 'porcentagem']].copy()
        df_retorno.rename(columns={
            'porcentagem': 'valor_acumulado'
        }, inplace=True)
        return df_retorno

    def get_registers(self):
        return self.valores.to_dict('records')

    def get_registers_by_date(self, data_inicio=None, data_fim=None):
        return self.valores.loc[
            (self.valores['data'].dt.date >= data_inicio)&
            (self.valores['data'].dt.date <= data_fim)
        ].to_dict('records')

    def get_registers_last_year(self):
        data_fim = datetime.today()
        data_inicio = data_fim - relativedelta(months=12)
        valor_acumulado = self.valores.loc[
            (self.valores['data'].dt.date >= data_inicio.date())&
            (self.valores['data'].dt.date <= data_fim.date()),
            'valor_acumulado'
        ].iloc[-1]
        return {"valor_acumulado": valor_acumulado}

