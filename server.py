from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import parse_qs
import uuid
import os
import requests

class ChatbotHandler(BaseHTTPRequestHandler):
    chat_histories = {}

    def get_session_id(self):
        return str(uuid.uuid4())

    def set_session_cookie(self, session_id):
        self.send_header('Set-Cookie', f'session_id={session_id}; HttpOnly; Path=/')

def do_GET(self):
    if self.path == '/':
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

        # Replace this URL with your actual GitHub Pages URL
        github_html_url = 'https://raw.githubusercontent.com/isml-educaional-chatbot/ChatBot1/main/index.html'

        # Fetch the HTML content from your GitHub repository
        response = requests.get(github_html_url)
        
        if response.status_code == 200:
            html_content = response.text
            self.wfile.write(html_content.encode('utf-8'))
        else:
            self.wfile.write(b'Failed to fetch HTML from GitHub.')

        session_id = self.get_session_id()
        self.set_session_cookie(session_id)
        chat_history = self.chat_histories.get(session_id, [])

    # The rest of your code for handling POST requests remains unchanged...



    def do_POST(self):

        user_message=""
        if self.path == '/':
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length).decode('utf-8')
            data = parse_qs(post_data)
            o=0
            try:
                user_message = data['user_message'][0]
            except:
                o=1
                pass
                
            
            # Process the user's message and get the bot's response

            bot_response= ""
            n=len(bot_response)
            f,e,j,z=0,0,0,0
            Subjects=["science", "physics", "chemistry", "biology"]
            physics = ["newton", "newtons", "first", "1st", "second", '2nd', 'third', '3rd', 'velocity', 'acceleration', 'force', 'work', 'kinetic energy', 'concave', 'convex' 'mirror formula']
            chemistry = ["law", "conservation", "constant", 'multiple', 'proportion', 'proportions', "periodic", 'table', 'reactivity', 'acid', 'base']
            biology = ["human body", "heart", "lungs", "respiration", "reproduction","photosyntesis", "dna", "evolution"]
            Pt= ["Hydrogen (H)", "Helium (He)", " Lithium (Li)", "Beryllium (Be)", "Boron (B)", "Carbon (C)", "Nitrogen (N)", "Oxygen (O)", "Fluorine (F)", "Neon (Ne)", "Sodium (Na)", "Magnesium (Mg)", "Aluminium (Al)", "Silicon (Si)", "Phosphorous (P)", "Sulfur (S)", "Chlorine (Cl)", "Argon (Ar)", "Potassium (K)", "Calcium (Ca)", "Scandium (Sc)", "Titanium (Ti)", "Vanadium (V)", "Chromium (Cr)", "Manganese (Mg)", "Iron (Fe)", "Cobalt (Co)", "Nickel (Ni)", "Copper (Cu)", "Zinc (Zn)"]
            ch="pt("
            
            if Subjects[0] in user_message.lower():
                if n==0:
                    bot_response=bot_response + "Science is the systematic study of the structure and behaviour of the physical and natural world through observation, experimentation, and the testing of theories against the evidence obtained. What about Science do you have concerns in? please enter one of the following:<br>Physics, Biology, Chemistry.<br>"
                    n=len(bot_response)
                elif n>0:
                    bot_response=bot_response + "And what about Science do you have concerns in? please enter one of the following:\nPhysics, Biology, Chemistry.<br>"
                    n=len(bot_response)
                z=1
           
            if Subjects[1] in user_message.lower():
                if n==0:
                    bot_response=bot_response + "Physics is the branch of science concerned with the nature and properties of matter and energy. The subject matter of physics includes mechanics, heat, light and other radiation, sound, electricity, magnetism, and the structure of atoms."
                    n=len(bot_response)
                elif n>0:
                    bot_response=bot_response + "And what about Physics do you need help in? I have information on:<br><strong>Newtons First law of motion, Newton's second law of motion, Newton's Third law of motion, And the formulas for:<br>Velocity,Acceleration,Force,Work, Kinetic energy.</strong><br>"
                    n=len(bot_response)
                z=1
            for i in physics[0:2]:
                if i in user_message.lower() and j==0:
                    j=1
                    for i in physics[2:4]:
                        if i in user_message.lower():
                            bot_response=bot_response + '''Newton's first law states that every object will remain at rest or in uniform motion in a straight line unless compelled to change its state by the action of an external force.<br> <strong>To learn more about Newton's laws of motion click</strong><a href="https://www1.grc.nasa.gov/beginners-guide-to-aeronautics/newtons-laws-of-motion/#:~:text=Newton%27s%20first%20law%20states%20that,action%20of%20an%20external%20force."> Here</a><br>'''
                    for i in physics[4:6]:
                        if i in user_message.lower():
                            bot_response=bot_response + '''Newton's second law of motion states that F = ma, or net force is equal to mass times acceleration. A larger net force acting on an object causes a larger acceleration, and objects with larger mass require more force to accelerate.<br> <strong>To learn more about Newton's laws of motion click</strong><a href="https://www1.grc.nasa.gov/beginners-guide-to-aeronautics/newtons-laws-of-motion/#:~:text=Newton%27s%20first%20law%20states%20that,action%20of%20an%20external%20force."> Here</a><br>'''
                    for i in physics[6:8]:
                        if i in user_message.lower():
                            bot_response=bot_response + '''Newton's Third Law of motion states that for every action (force) in nature there is an equal and opposite reaction. If object A exerts a force on object B, object B also exerts an equal and opposite force on object A. In other words, forces result from interactions.<br> <strong>To learn more about Newton's laws of motion click</strong><a href="https://www1.grc.nasa.gov/beginners-guide-to-aeronautics/newtons-laws-of-motion/#:~:text=Newton%27s%20first%20law%20states%20that,action%20of%20an%20external%20force."> Here</a><br>'''
                    for i in physics[2:8]:
                        if i in user_message.lower():
                            f=1
                    if f==0 and e==0:
                        bot_response= bot_response + "Isaac Newton is popularly remembered as the man who saw an apple fall from a tree, and was inspired to invent the theory of gravity. If you have grappled with elementary physics then you know that he invented calculus and the three laws of motion upon which all of mechanics is based.<br>"
                        e=1
                    z=1
            if physics[13] in user_message.lower():
                bot_response = bot_response + "Concave mirrors have a curved inward reflective surface. They reflect light inward towards a focal point. The image formed by a concave mirror varies based on the distance between the object and the mirror."
                bot_response = bot_response + 'Here is an example of light reflecting off a concave mirror: <br><br><img src="https://media.tenor.com/EQtazsIKn0YAAAAC/reflection-light.gif" alt="Image" height="200" width="300"><br>'
                z=1
            if physics[14] in user_message.lower():
                bot_response = bot_response + "The convex mirror has a reflecting surface that curves outward, resembling a portion of the exterior of a sphere. Light rays parallel to the optical axis are reflected from the surface in a direction that diverges from the focal point, which is behind the mirror"
                bot_response = bot_response + ' Here is an example of light reflecting off a convex mirror: <br><br><img src="https://media.tenor.com/X1cAZjCk03YAAAAC/reflection-light.gif" alt="Image" height="200" width="300"><br>'
                z=1
            if "mirror formula" in user_message.lower():
                bot_response = bot_response + 'Here is how you find the mirror formula:<br><br>  <iframe width="560" height="315" src="https://www.youtube.com/embed/TwaE8nZMOBw" frameborder="0" allowfullscreen></iframe><br>'
                z=1
            f=0
            if physics[8] in user_message.lower():
                bot_response=bot_response + "Formula of velocity, v = S / t<br>"
                z=1
            if physics[9] in user_message.lower():
                bot_response=bot_response + "Formula of acceleration, a = v / t<br>"
                z=1
            if physics[10] in user_message.lower():
                bot_response=bot_response + "Formula of force, F = m x a<br>"
                z=1
            if physics[11] in user_message.lower():
                bot_response=bot_response + "Formula of work, W = F x S<br>"
                z=1
            if physics[12] in user_message.lower():
                bot_response=bot_response + "Formula of kinetic energy, K = 1/2 x m x v²<br>"
                z=1
            
            if Subjects[2] in user_message.lower():
                bot_response = bot_response + "Chemistry is the branch of science concerned with the substances of which matter is composed, the investigation of their properties and reactions, and the use of such reactions to form new substances. <br>"
                z=1
            if chemistry[0] in user_message.lower():
                if chemistry[1] in user_message.lower():
                    for i in chemistry[2:6]:
                        if i in user_message.lower():
                            f=1
                    if f==0:
                       bot_response= bot_response + "The law of conservation of mass states that mass within a closed system remains the same over time.<br>"
                    else:
                        bot_response=bot_response+ "I do not understand. Check if there are any spelling errors or incorrect laws entered<br>"
                        f=0
                        z=1
                if chemistry[2] in user_message.lower() and chemistry[3] not in user_message.lower():
                    for i in chemistry[4:6]:
                        if f==0:
                            if i in user_message.lower():
                                f=1
                                bot_response=bot_response + "The law of constant proportions states that chemical compounds are made up of elements that are present in a fixed ratio by mass. This implies that any pure sample of a compound, no matter the source, will always consist of the same elements that are present in the same ratio by mass.<br>"
                                z=1
                    f=0

                if chemistry[3] in user_message.lower() and chemistry[2] not in user_message.lower():
                    for i in chemistry[4:6]:
                        if f==0:
                            if i in user_message.lower():
                                f=1
                                bot_response=bot_response + "The law of multiple proportions states that whenever the same two elements form more than one compound, the different masses of one element that combine with the same mass of the other element are in the ratio of small whole numbers.<br>"
                    f=0
                    z=1
            for i in chemistry[6:8]:
                if f==0:
                    if i in user_message.lower():
                        bot_response = bot_response + 'Here is the periodic table: <br><img src="https://www.periodictable.co.za/media/periodic-table-col-download.png" alt="Image" height="650" width="1000"><br>'
                        f=1
                        z=1
            f=0
            if ch in user_message.lower():
                if len(user_message) == 5:
                    try:
                        no=int(user_message[3])
                    except:
                        f=1
                        pass
                    if f==0:
                        if int(user_message[3]) <=0:
                            bot_response=bot_response + "Please enter a valid number only from 1 to 30<br>"
                        else:
                            bot_response=bot_response + Pt[no-1] + "<br>"
                        z=1
                elif len(user_message) == 6:
                    try:
                        no=int(user_message[3])
                        no=no*10
                        no=no + int(user_message[4])
                    except:
                        f=1
                        pass
                    if f==0:
                        if no >30:
                            bot_response=bot_response + "Please enter a valid number only from 1 to 30. <br>"
                        else:
                            bot_response=bot_response + Pt[no-1] + "<br>"
                        z=1
                f=0
            if chemistry[8] in user_message.lower():
                bot_response=bot_response+'Here is the table of reactivity in metals: <br><img src="https://cdn1.byjus.com/wp-content/uploads/2019/06/Activity-Series-of-Metals-Updated.png" alt="Image" height="650" width="800"><br>'
                z=1
            if chemistry[9] in user_message.lower():
                z=1
                bot_response=bot_response+'''acids are substances with particular chemical properties including turning litmus red, neutralizing alkalis, and dissolving some metals; typically, a corrosive or sour-tasting liquid of this kind.<strong>To learn more about acids and bases click this link:<br><br> <a href="https://byjus.com/chemistry/acids-and-bases/"> Here</a><br>'''
            if chemistry[10] in user_message.lower():
                bot_response=bot_response + '''A base is a substance that can neutralize the acid by reacting with hydrogen ions. Most bases are minerals that react with acids to form water and salts. Bases include the oxides, hydroxides and carbonates of metals. The soluble bases are called alkalis. Sodium hydroxide is an alkali. <strong>To learn more about acids and bases click this link:<br><br> <a href="https://byjus.com/chemistry/acids-and-bases/"> Here</a><br>'''
                z=1

            if Subjects[3] in user_message.lower():
                bot_response=bot_response+ "Biology is the study of living organisms, divided into many specialized fields that cover their morphology, physiology, anatomy, behaviour, origin, and distribution.<br>"
            if biology[0] in user_message.lower():
                bot_response= bot_response + 'Here is the human body: <br><img src="https://upload.wikimedia.org/wikipedia/commons/d/d9/Internal_organs.png" alt="Image" height="800" width="700"><br>'
            if biology[1] in user_message.lower():
                bot_response = bot_response + 'The heart pumps blood around your body as your heart beats. This blood sends oxygen and nutrients to all parts of your body, and carries away unwanted carbon dioxide and waste products.<br>'
            if biology[2] in user_message.lower():
                bot_response=bot_response+'The lungs and respiratory system allow us to breathe. They bring oxygen into our bodies (called inspiration, or inhalation) and send carbon dioxide out (called expiration, or exhalation). This exchange of oxygen and carbon dioxide is called respiration.<br>'
            if biology[3] in user_message.lower():
                bot_response=bot_response +'respiration is the movement of oxygen from the outside environment to the cells within tissues, and the removal of carbon dioxide in the opposite direction thats to the environment.<br>'
            if biology[4] in user_message.lower():
                bot_response=bot_response+'Reproduction is the biological process by which new individual organisms – "offspring" – are produced from their "parent" or parents. Reproduction is a fundamental feature of all known life; each individual organism exists as the result of reproduction. There are two forms of reproduction: asexual and sexual.<br>'
            if biology[5] in user_message.lower():
                bot_response=bot_response+'photosynthesis is a biological process used by many cellular organisms to convert light energy into chemical energy, which is stored in organic compounds that can later be metabolized through cellular respiration to fuel the organisms activities.<br>'
            if biology[6] in user_message.lower():
                bot_response=bot_response+'Deoxyribonucleic acid is a polymer composed of two polynucleotide chains that coil around each other to form a double helix. The polymer carries genetic instructions for the development, functioning, growth and reproduction of all known organisms and many viruses. DNA and ribonucleic acid are nucleic acids.<br>'
            if biology[7] in user_message.lower():
                bot_response=bot_response+'evolution is the change in heritable characteristics of biological populations over successive generations.<br>'
            
            if len(bot_response)==0:
                bot_response=bot_response+"I did not understand your message, could you please check for any spelling errors?<br>"

            
            if o==0:
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                history=""
                for i in chat_history:
                    history=history + i
                history_html=f'<p>{history}</p>'
                response_html = f'<p style="color: #3b9c32;"><strong>You:</strong> {user_message}</p><p style="color: #323dd1;"><strong>Bot:</strong> {bot_response}</p>'    
                self.wfile.write(history_html.encode('utf-8'))                      
                self.wfile.write(response_html.encode('utf-8'))
                chat_history.append(response_html)
            else:
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                response_html = f'<p style="color: #b1b1b1;">Please enter something.</p>'
                self.wfile.write(response_html.encode('utf-8'))    
                chat_history.append(response_html)
def run():
    port = int(os.environ.get("PORT", 8000))  # Use the PORT environment variable if available, or default to 8000
    server_address = ('', port)
    httpd = HTTPServer(server_address, ChatbotHandler)
    print(f'Server started on port {port}')
    httpd.serve_forever()

if __name__ == '__main__':
    run()

if __name__ == '__main__':
    run()