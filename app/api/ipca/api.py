from flask_restx import Namespace, Resource, fields, reqparse, inputs
import logging

from app.models.ipca import IpcaModel

api = Namespace("ipca", description="IPCA related operations")

ipca = api.model(
    "IPCA",
    {
        "data": fields.Date(required=False, description="Data da análise"),
        "valor_acumulado": fields.Float(required=False, description="Valor no dia"),
    },
)

parser = reqparse.RequestParser()
parser.add_argument('data_inicio', type=inputs.date_from_iso8601, required=False, location='args', help='Data inicial')
parser.add_argument('data_fim', type=inputs.date_from_iso8601, required=False, location='args', help='Data final')


@api.route("/")
class IpcaList(Resource):
    @api.doc("list_ipca")
    @api.marshal_list_with(ipca)
    @api.expect(parser)
    def get(self):
        """List all ipca"""
        api.logger.info("Request GET para dados IPCA")
        ipca = IpcaModel()
        args = parser.parse_args()
        data_inicio = args.get('data_inicio', None)
        data_fim = args.get('data_fim', None)
        if data_inicio is not None and data_fim is not None:
            return ipca.get_registers_by_date(data_inicio, data_fim)
        return ipca.get_registers()

@api.route("/year/")
class IpcasLastYear(Resource):
    @api.doc("lista_ipca_ultimo_ano")
    def get(self):
        """Valor Acumulado Ultimo Ano"""
        api.logger.info("Request GET para dados acumulado do ultimo ano ")
        ipca = IpcaModel()
        return ipca.get_registers_last_year()