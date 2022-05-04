# Author, David Martinez (@dx0xm)(david.martinez@spark.co.nz)

import os, json, datetime, smtplib
from openpyxl import Workbook
from openpyxl.styles import Alignment
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from os import listdir

def read_file(dstfile):
    ret = []
    try:
        with open(dstfile, 'r') as fread:
            contents = fread.readlines()
            [ret.append(x.strip('\n')) for x in contents if x != '\n']
    except:
        return []
   
    return ret


def save_file(lst, dstfile):
    with open(dstfile, 'w') as writeFile:
        for dev in lst:
            line = dev + '\n'
            writeFile.write(line)

def create_report(data):

#    if ';' in email:
#        #Multiple emails, split in a list
#        email = [x.strip() for x in email.split(';')]
#        for e in email:
#            if not '@spark.co.nz' in e:
#                raise ("Error checking email: Please supply only @spark.co.nz email address.")
#    else:
#     if not '@spark.co.nz' in email:
#         raise ("Error checking email: Please supply @spark.co.nz email.")

    #report_name = 'output_' + str(datetime.datetime.now().strftime("%Y-%m-%d-%H-%M")) + '.xlsx'

#    wb = Workbook()
#    ws1 = wb.active
#    ws1.title = "main"
#    ws1['A1'] = 'Device Name'
#    ws1['B1'] = 'Command Output'

#    num = 2
#    for device, output in data.items():

#        ws1[f'A{num}'] = device
#        for line in output:
#            ws1[f'B{num}'] = str(ws1[f'B{num}'].value) + f'{str(line) + " "}\n'

#        ws1[f'A{num}'].alignment  = Alignment(vertical='top')
#        ws1[f'B{num}'].alignment  = Alignment(vertical='top', wrap_text=True)

#        ws1.column_dimensions['A'].width = 20
#        ws1.column_dimensions['B'].width = 50
#        num += 1
    
#    wb.save(filename=report_name)

#    attachments = [report_name]
    email = 't828744@spark.co.nz'
    data = MIMEMultipart()
    data['From'] = 'sdpjenkins@spark.co.nz'
#    if isinstance(email, list):
#        data['To'] = ';'.join(email)
#    else:
#        data['To'] = email
    data['To'] = email
    data['Subject'] = 'Jenkins Job: IR TaaS CName details'
    data.attach(MIMEText('CName report has been attached to this email.', 'plain'))
#    for item in attachments:
#        attachment = open(item, "rb")
#        p = MIMEBase('application', 'octet-stream')
#        p.set_payload((attachment).read())
#        encoders.encode_base64(p)
#        p.add_header('Content-Disposition', f'attachment; filename={item}')
#        data.attach(p)
    smtp = smtplib.SMTP('122.56.66.9')
    text = data.as_string()
    smtp.sendmail('sdpjenkins@spark.co.nz', 'email', text)
    smtp.quit()
    print(f'Status Report has been sent to {email}')

def main():
    sender_email = "sdpjenkins@spark.co.nz"
    receiver_email = os.getenv('_EMAIL') #"t828744@spark.co.nz"
    subject = "IR TaaS CName details"
    body = "This message is sent by Python from Jenkins job 'taas_ASA_quarterly_audits'."
    
    filenames = os.listdir('auditfiles')
    print(filenames)
    finalfile = 'audit_report_' + str(datetime.datetime.now().strftime("%Y-%m-%d-%H-%M")) + '.txt'
    with open(finalfile, "w") as outfile:
        for fn1 in filenames:
            with open('auditfiles/'+fn1) as infile:
                contents = infile.read()
                outfile.write(contents)
                outfile.write("\n==================================\n==================================\n==================================\n")
            outfile.write("\n")

    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = subject
    msg.attach(MIMEText(body,'plain'))

    attachmentname = finalfile
    attachment = open(attachmentname,'rb')

    part = MIMEBase('application','octet-stream')
    part.set_payload((attachment).read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition',"attchment; filename= "+attachmentname)

    msg.attach(part)
    body_str = msg.as_string()
     
    # Send email here
    server = smtplib.SMTP('122.56.66.9')
    server.sendmail(sender_email, receiver_email, body_str)
    server.quit()
    print(f'Status Report has been sent to {receiver_email}')
#    report = dict()
#    for f in os.listdir(os.getcwd()+'/files'):
#        if '.txt' in f:
#            print(f)
#            out = read_file(os.getcwd()+'/files/'+f)
#            report.update({f.replace('.txt', ''): out})
#            [print(x) for x in out]

#    if report and os.getenv('EMAIL'):
#    create_report()
    # try:
    #     with open('taas_devices.json', 'r') as json_file:
    #         devices = json.load(json_file)
    # except Exception as e:
    #     print(str(e))
    #     return 0

    # finalEntries = ['[taasdevices]']
    # # finalEntries = []
    # for name,status in devices.items():
    #     if ('001' in name or '051' in name)and status == 'poweredOn':
    #         fqdn = name + '.gnet.svns.net.nz'
    #         if resolve_dns(fqdn):
    #             finalEntries.append(fqdn)
    #         else:
    #             print(f'{fqdn} did not resolve dns')
    # if len(finalEntries) > 1:
    #     #PMP setup
    #     PMP_TOKEN = os.environ['PMP_TOKEN']
    #     PMP_URL = os.environ['PMP_URL']
    #     pmp_object = pmp(PMP_URL, PMP_TOKEN)
    #     if pmp_object.error is not None:
    #         print(pmp_object.error)
    #         return 0     

    #     pass_obj, error = pmp_object.get_credentials_for_account('ansible_res', 'svc-cpa-ansible-taas')
    #     if error is not None:
    #         print("Error retrieving password from PMP: " + str(error))
    #         return 0    
    #     pwd = pass_obj['PASSWORD'] 
    #     finalEntries += ['[taasdevices:vars]', 'ansible_network_os=asa', 'ansible_user=svc-cpa-ansible-taas', f'ansible_ssh_pass={pwd}']
    #     save_file(finalEntries, 'inventory.inv')
    # else:
    #     save_file([], 'inventory.inv')
    # [print(x) for x in finalEntries]

if __name__ == "__main__":
    main()
