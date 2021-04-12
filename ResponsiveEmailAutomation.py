import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

style = '"margin: 10px;font-size:72px;"'

sender_email = "YourAutomationEnabledEmailAccount"
receiver_email = "Target Audience"
password = "YourPassword"

message = MIMEMultipart("alternative")
message["Subject"] = "Test Email Campaign"
message["From"] = sender_email
message["To"] = receiver_email

# Create the plain-text and HTML version of your message
text = """\
Hi,
How are you?
This message was sent via Python. It is meant to be viewed in HTML."""
html = """<!DOCTYPE html>
<html lang="en" xmlns="http://www.w3.org/1999/xhtml" xmlns:o="urn:schemas-microsoft-com:office:office">
<head>
	<meta charset="utf-8">
  <meta name="viewport" content="width=device-width,initial-scale=1">
  <meta name="x-apple-disable-message-reformatting">
  <title></title>
	<!--[if mso]>
  <style>
    table {border-collapse:collapse;border-spacing:0;border:none;margin:0;}
    div, td {padding:0;}
    div {margin:0 !important;}
	</style>
  <noscript>
    <xml>
      <o:OfficeDocumentSettings>
        <o:PixelsPerInch>96</o:PixelsPerInch>
      </o:OfficeDocumentSettings>
    </xml>
  </noscript>
  <![endif]-->
  <style>
    table, td, div, h1, p {
      font-family: Arial, sans-serif;
    }
    @media screen and (max-width: 530px) {
      .unsub {
        display: block;
        padding: 8px;
        margin-top: 14px;
        border-radius: 6px;
        background-color: #88A1D8;
        text-decoration: none !important;
        font-weight: bold;
      }
      .col-lge {
        max-width: 100% !important;
      }
    }
    @media screen and (min-width: 531px) {
      .col-sml {
        max-width: 27% !important;
      }
      .col-lge {
        max-width: 85% !important;
      }
    }
  </style>
</head>
<!-- background -->
<body style="margin:0;padding:0;word-spacing:normal;background-color:#88A1D8;">
  
    <!--greybackground-->
    <div role="article" aria-roledescription="email" lang="en" style="text-size-adjust:100%;-webkit-text-size-adjust:100%;-ms-text-size-adjust:100%;background-color: #697CA5;">

    <!--infoContainer-->
    <table role="presentation" style="width:100%;border:none;border-spacing:0;">
      <tr>
        <td align="center" style="padding:0;">
          <!--[if mso]>
          <table role="presentation" align="center" style="width:600px;">
          <tr>
          <td>
          <![endif]-->
            
          <!-- content table font-color parent-->        
          <table role="presentation" style="width:95%;max-width:600px;border:none;border-spacing:0;text-align:left;font-family:Arial,sans-serif;font-size:16px;line-height:22px;color:#2B5C8C;">
            
            <tr>
              <td style="padding:0;font-size:24px;line-height:28px;font-weight:bold;background-color: white;">
                <a href="https://www.dreamadaptive.org/" style="text-decoration:none;"><img src="https://www.dreamadaptive.org/wp-content/uploads/2019/06/FULL_COLORDREAM_LOGO-e1601413320951.png" width="600" alt="" style="width:80%;height:auto;display:block;border:none;text-decoration:none;color:white;margin: 0 auto; padding-top: 30px"></a>
              </td>
            </tr>  
              
            <!--content container 1 -->
            <tr>
              <td style="padding:20px 30px 30px 30px;text-align:center;font-size:24px;font-weight:bold;background-color: white;">
                  
                <div class="col-lge" style="display: inline-block;width:100%;max-width:395px;vertical-align:top;padding-bottom:20px;font-family:Arial,sans-serif;font-size:16px;line-height:22px;color:#2B5C8C;">  
                <h1 style="margin:0 auto;font-size:24px;line-height:32px;font-weight:bold;letter-spacing:-0.02em;">Join Us For Our 2nd Annual:</h1><h2 style="margin-top: 0">Shred-A-Thon</h2>
                <p style="margin-top:0;margin-bottom:12px;font-size: 0.9em;">
                    Fundraise within your circle in advance of the event to support DREAM.</p> 
                 <p style="margin-top:0;margin-bottom:12px;font-size: 0.9em;">   
                    Then join us for a fun vertical challenge on March 27th; ski or ride as many vertical feet as you can in one day. </p>

                  <p style="margin-top:0;margin-bottom:0px;font-size: 0.9em;">Prizes for most funds raised & vertical feet skied in multiple categories.</p>
                </div>
                  
              </td>        
            </tr>
        
            
            <!--content container 3 -->  
            
              
            <tr>
              <td style="padding:0;font-size:24px;line-height:28px;font-weight:bold;">
                <a href="https://www.dreamadaptive.org/events/shred/" style="text-decoration:none;"><img src="https://www.dreamadaptive.org/wp-content/uploads/2019/02/Powder-Camp-Main-1461x547.jpg" width="600" alt="" style="width:100%;height:auto;display:block;border:none;text-decoration:none;color:#363636;"></a>
              </td>
            </tr>
            
            <!-- content container 4-->  
            <tr>
              <!-- left item block -->
                <td style="padding-left: 30px;padding-right: 30px; pfont-size:0;background-color:#ffffff;border-bottom:1px solid #f0f0f5;border-color:rgba(201,201,207,.35);">
                <!--[if mso]>
                
                <td style="width:395px;padding-bottom:20px;" valign="top">
                <![endif]-->
                
                <!--right item block-->    
                <div class="col-lge" style="display:inline-block;width:100%;max-width:90%;vertical-align:top;padding-bottom:20px;font-family:Arial,sans-serif;font-size:16px;line-height:22px;color:#2B5C8C;">
                  
                <h2>OVERVIEW: <img src="https://www.dreamadaptive.org/wp-content/uploads/2019/12/yeti.png" width="115" alt="" style=";max-width:115px;margin-bottom:20px;"></h2>
                   
                <ul>
                    <li>To attend you must raise at least $200 for DREAM ($250 if you need a day lift ticket) by March 27th.</li>
                    <li>Use the DREAM fundraising platform to create a fundraising page to share with your family & friends</li>
                    <li>Create a fundraising team for an even better chance to win prizes!</li>
                    <li>Hike, ski, or ride bell-to-bell or as much as you can take on March 27th, 2020; vertical feet will be tallied & prizes awarded</li>
                    <li>Head to an outdoor ski-in/ski-out private residence that afternoon to celebrate!</li>

                </ul>
                  
                  <p style="margin:0;">
                    <!--button-->
                    <a href="https://dreamadaptive.z2systems.com/np/clients/dreamadaptive/createFundraiser.jsp?campaignId=81&" style="background: #2B5C8C; text-decoration: none; padding: 10px 25px; color: #ffffff; border-radius: 4px; display:inline-block; mso-padding-alt:0;text-underline-color:#2B5C8C; margin-left: 40px;margin-top: 10px"><!--[if mso]><i style="letter-spacing: 25px;mso-font-width:-100%;mso-text-raise:20pt">&nbsp;</i><![endif]-->
                        <span style="mso-text-raise:10pt;font-weight:bold;">FUNDRAISE</span><!--[if mso]><i style="letter-spacing: 25px;mso-font-width:-100%">&nbsp;</i><![endif]-->
                    </a>
                  </p> 
                    
                </div>
                </td>    
                <!--[if mso]>
                </td>
                </tr>
                </table>
                <![endif]-->
              </td>
            </tr>
            
            <!-- content block 5 -->  
            <tr>
              <td style="padding:30px;font-size:24px;line-height:28px;font-weight:bold;background-color:#ffffff;border-bottom:1px solid #f0f0f5;border-color:rgba(201,201,207,.35);">
                <a href="https://www.dreamadaptive.org/events/shred/" style="text-decoration:none;"><img src="https://www.dreamadaptive.org/wp-content/uploads/2021/02/Shred-A-Thon-Poster-2021-pdf-791x1024.jpg" width="540" alt="" style="width:100%;height:auto;border:none;text-decoration:none;color:#363636;"></a>
              </td>
            </tr>
            
            <!-- content block 6 -->  
              
            <tr>
              <td style="padding:30px 30px 0px 30px;background-color:#ffffff;">
                <h2 style="margin:0;">WHAT YOU RECEIVE:</h2>
                  <ul>
                    <li>Complimentary light breakfast & coffee @ the DREAM Shack</li>
                    <li>Access to a discounted lift ticket (included in your fundraising minimum), if needed. Must notify us by March 20th if you need a lift ticket.</li>  
                    <li>9:00am-4:00pm vertical challenge for those interested; or just ski with friends and Shred the love!</li>
                    <li>Hot Lunch…from a local yummy food truck</li>
                    <li>Prizes for top individual and team fundraisers</li>
                    <li>Prizes for top competitors in each division, for most vertical feet shredded</li>
                    <li>Post-party with awards, libations, and music</li>
                    <li>Snacks, coffee, and stoke all day long to keep you shredding the laps!</li>  
                  </ul>

              </td>
            </tr>
              
            <tr>
              <td style="padding-bottom:30px;background-color:#ffffff;">
                <p style="margin:0 auto;">
                    <!--button-->
                    <a href="mailto:jtickle@dreamadaptive.org" style="background: #2B5C8C; text-decoration: none; padding: 10px 25px; color: #ffffff; border-radius: 4px; display:inline-block; mso-padding-alt:0;text-underline-color:#2B5C8C; margin: 0px 0px 0px 70px;"><!--[if mso]><i style="letter-spacing: 25px;mso-font-width:-100%;mso-text-raise:20pt">&nbsp;</i><![endif]-->
                        <span style="mso-text-raise:10pt;font-weight:bold;">Contact Us</span><!--[if mso]><i style="letter-spacing: 25px;mso-font-width:-100%">&nbsp;</i><![endif]-->
                    </a>
                  </p> 
                </td>
            </tr>
              
              
            
              <!--footer-->
              <tr>
              <td style="padding:30px;text-align:center;font-size:12px;background-color:#404040;color:#cccccc;">
                <p style="margin:0 0 8px 0;"><a href="https://www.facebook.com/pg/dreamadaptivemontana/posts/" style="text-decoration:none;"><img src="https://assets.codepen.io/210284/facebook_1.png" width="40" height="40" alt="f" style="display:inline-block;color:#cccccc;"></a> <a href="https://www.instagram.com/dreamadaptivemontana/?hl=en" style="text-decoration:none;"><img src="https://assets.codepen.io/210284/twitter_1.png" width="40" height="40" alt="t" style="display:inline-block;color:#cccccc;"></a></p>
                <p style="margin:0;font-size:14px;line-height:20px;">&reg; Dream Adaptive 2021<br><a class="unsub" href="http://www.example.com/" style="color:#cccccc;text-decoration:underline;">Unsubscribe instantly</a></p>
              </td>
            </tr>
          </table>
          <!--[if mso]>
          </td>
          </tr>
          </table>
          <![endif]-->
        </td>
      </tr>
    </table>
  </div>
</body>
</html>"""

# Turn these into plain/html MIMEText objects
part1 = MIMEText(text, "plain")
part2 = MIMEText(html, "html")

# Add HTML/plain-text parts to MIMEMultipart message
# The email client will try to render the last part first
message.attach(part1)
message.attach(part2)

# Create secure connection with server and send email
context = ssl.create_default_context()
with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(
        sender_email, receiver_email, message.as_string()
    )
