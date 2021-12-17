from flask import Flask, jsonify
from flask_restful import Api
from dotenv import load_dotenv
from flask_cors import CORS

from resources.authenticate.sys_auth_routes import fn_sys_auth_initialize_routes
from resources.inventory.inv_routes import fn_inv_initialize_routes
from resources.reports.dashboards.dashboard_routes import fn_dashboard_initialize_routes
from resources.sales.sls_routes import fn_sls_initialize_routes
from resources.reports.pdfs.pdf_routes import fn_pdfs_initialize_routes
from resources.organization.org_routes import fn_org_initialize_routes
from resources.system.sys_routes import fn_sys_initialize_routes
from resources.security.sec_routes import fn_sec_initialize_routes
from resources.account.act_routes import fn_act_initialize_routes
from resources.crm.crm_routes import fn_crm_initialize_routes
from resources.utils.crypto.sys_crypto_routes import fn_sys_crypto_routes
from resources.service.srv_routes import fn_srv_initialize_routes
from resources.communication.old_sms.sms_routes import fn_sms_initialize_routes
from resources.communication.old_email.email_routes import fn_email_initialize_routes
from resources.communication.old_whatsapp.whatsapp_routes import fn_whatsapp_initialize_routes
from resources.document.fileManagement.doc_routes import fn_doc_file_management_initialize_routes
from resources.school.sch_routes import fn_sch_initialize_routes
from resources.communication.IndividualMessage.individual_message_routes import fn_individual_message_initialize_routes
from resources.utils.AWS.aws_routes import fn_comm_aws_initialize_routes
from resources.communication.sms.sms_routes import fn_comm_sms_initialize_routes
from resources.communication.batchHistory.batch_history_routes import fn_comm_batch_history_initialize_routes
from resources.communication.batchEmail.email_routes import fn_comm_email_initialize_routes
from resources.communication.batchWhatsapp.whatsapp_routes import fn_comm_whatsapp_initialize_routes
from resources.communication.productMessage.product_routes import fn_com_product_message_initialize_routes
from resources.vehicle.vhc_routes import fn_vhc_initialize_routes
from resources.communication.ssm.ssm_routes import fn_comm_ssm_initialize_routes
from resources.communication.communicationMessage.comm_message_routes import fn_com_message_initialize_routes
from resources.rewards.rwd_routes import fn_rwd_initialize_routes
from resources.transport.trns_routes import fn_trns_initialize_routes
from resources.home.hom_routes import fn_hom_initialize_routes
from resources.ngo.ngo_routes import fn_ngo_initialize_routes
from resources.communication.school.school_routes import  fn_com_school_initialize_routes
from resources.ordermanagement.odr_routes import  fn_odr_initialize_routes



# Lookups paths
from resources.lookups.inventory.lkp_inv_routes import fn_lkp_inv_initialize_routes
from resources.lookups.organization.lkp_org_routes import fn_lkp_org_initialize_routes
from resources.lookups.account.lkp_act_routes import fn_lkp_act_initialize_routes
from resources.lookups.crm.lkp_crm_routes import fn_lkp_crm_initialize_routes
from resources.lookups.system.lkp_sys_routes import fn_lkp_sys_initialize_routes
from resources.lookups.communication.lkp_com_routes import fn_lkp_com_initialize_routes
from resources.lookups.school.lkp_sch_routes import fn_lkp_sch_initialize_routes
from resources.lookups.document.lkp_doc_routes import fn_lkp_doc_initialize_routes
from resources.lookups.security.lkp_sec_routes import fn_lkp_sec_initialize_routes
from resources.lookups.service.lkp_srv_routes import fn_lkp_srv_initialize_routes
from resources.lookups.vehicle.lkp_vhc_routes import fn_lkp_vhc_initialize_routes
from resources.lookups.sales.lkp_sls_routes import fn_lkp_sls_initialize_routes
from resources.lookups.rewards.lkp_rwd_routes import fn_lkp_rwd_initialize_routes
from resources.lookups.transport.lkp_tpt_routes import fn_lkp_tpt_initialize_routes
from resources.lookups.ngo.lkp_ngo_routes import fn_lkp_ngo_initialize_routes
from resources.lookups.orderManagement.lkp_odm_routes import fn_lkp_odm_initialize_routes
from shared import read_image

app = Flask(__name__)
CORS(app, resources={r"/api/*": {"origins": "*"}})
api = Api(app)


# Route
fn_sys_auth_initialize_routes(api)
fn_inv_initialize_routes(api)
fn_dashboard_initialize_routes(api)
fn_sls_initialize_routes(api)
fn_pdfs_initialize_routes(api)
fn_org_initialize_routes(api)
fn_sys_initialize_routes(api)
fn_sec_initialize_routes(api)
fn_act_initialize_routes(api)
fn_crm_initialize_routes(api)
fn_sys_crypto_routes(api)
fn_srv_initialize_routes(api)
fn_sms_initialize_routes(api)
fn_email_initialize_routes(api)
fn_whatsapp_initialize_routes(api)
fn_doc_file_management_initialize_routes(api)
fn_sch_initialize_routes(api)
fn_individual_message_initialize_routes(api)
fn_comm_aws_initialize_routes(api)
fn_comm_sms_initialize_routes(api)
fn_comm_batch_history_initialize_routes(api)
fn_comm_email_initialize_routes(api)
fn_comm_whatsapp_initialize_routes(api)
fn_com_product_message_initialize_routes(api)
fn_vhc_initialize_routes(api)
fn_comm_ssm_initialize_routes(api)
fn_com_message_initialize_routes(api)
fn_rwd_initialize_routes(api)
fn_trns_initialize_routes(api)
fn_hom_initialize_routes(api)
fn_ngo_initialize_routes(api)
fn_com_school_initialize_routes(api)
fn_odr_initialize_routes(api)



fn_lkp_inv_initialize_routes(api)
fn_lkp_org_initialize_routes(api)
fn_lkp_act_initialize_routes(api)
fn_lkp_crm_initialize_routes(api)
fn_lkp_sys_initialize_routes(api)
fn_lkp_com_initialize_routes(api)
fn_lkp_sch_initialize_routes(api)
fn_lkp_doc_initialize_routes(api)
fn_lkp_sec_initialize_routes(api)
fn_lkp_srv_initialize_routes(api)
fn_lkp_vhc_initialize_routes(api)
fn_lkp_sls_initialize_routes(api)
fn_lkp_rwd_initialize_routes(api)
fn_lkp_tpt_initialize_routes(api)
fn_lkp_ngo_initialize_routes(api)
fn_lkp_odm_initialize_routes(api)


# @app.route('/image')
# def test():
#     return jsonify({"base64": read_image('bofa', 'test.png', 'tss-test-bucket')})


if __name__ == "__main__":
    load_dotenv()
    app.run()
