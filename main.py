import streamlit as st
from PIL import Image
from gtts import gTTS
import requests
import tempfile
from io import BytesIO

# Title of the app
st.title('HOPEHUB')
# Introduction to the app
st.subheader("""
    This app provides emergency guidance for both medical and non-medical situations.
    Select an emergency type by clicking a button or using your voice.
""")

# Medical emergency data with URLs instead of file paths
medical_emergency_data = {
    "heart attack": {
        "description": """
*Recognizing a Heart Attack:*
- Chest pain or discomfort, often described as pressure, squeezing, or fullness.
- Pain or discomfort in other areas of the upper body, such as arms, back, neck, jaw, or stomach.
- Shortness of breath.
- Cold sweat, nausea, or lightheadedness.

*What to Do:*
1. *Call Emergency Services (911 or local emergency number) Immediately:*
   - Provide clear information about your location and the situation.
2. *Chew and Swallow an Aspirin (if not allergic):*
   - Aspirin can help reduce blood clotting and improve blood flow.
3. *Begin CPR if the Person is Unconscious:*
   - *For CPR:*
     - Place the person on their back on a firm surface.
     - Place the heel of one hand on the center of the chest, then place the other hand on top.
     - Perform chest compressions at a rate of 100-120 per minute and a depth of at least 2 inches (5 cm).
4. *Use an Automated External Defibrillator (AED) if Available:*
   - Follow the AED’s voice prompts to deliver a shock if advised.
5. *Stay Calm and Provide Reassurance:*
   - Keep the person calm and avoid unnecessary movement.

*Aftercare:*
- Continue to monitor the person’s condition until emergency responders arrive.
- If the person becomes unconscious, continue CPR until help arrives or the person shows signs of recovery.
        """,
        "image": "https://www.ckbhospital.com/wp-content/uploads/2022/05/First-Aid-during-heart-attack-CPR-Guide-step-by-step-1024x576.jpg"  # Replace with actual URL
    },
    "stroke": {
        "description": """
*Recognizing a Stroke: FAST Method:*
- *Face:* Ask the person to smile. Does one side of the face droop?
- *Arms:* Ask the person to raise both arms. Does one arm drift downward?
- *Speech:* Ask the person to repeat a simple sentence. Is their speech slurred or strange?
- *Time:* If you observe any of these signs, call emergency services immediately.

*What to Do:*
1. *Call Emergency Services Immediately:*
   - Time is critical in minimizing brain damage.
2. *Ensure the Person is Safe and Comfortable:*
   - Help them sit or lie down in a safe position.
3. *Check for Breathing and Responsiveness:*
   - If the person is unresponsive and not breathing, begin CPR.
4. *Do Not Give Food or Drink:*
   - Avoid potential choking hazards if the person has difficulty swallowing.
5. *Stay Calm and Provide Reassurance:*
   - Keep the person calm and avoid unnecessary movement.

*Aftercare:*
- Monitor the person’s condition until emergency responders arrive.
- If the person becomes unconscious, continue CPR until help arrives or the person shows signs of recovery.
        """,
        "image": "https://i.pinimg.com/originals/4b/84/15/4b8415035a3dbde9081cf58bca11a3ba.jpg"  # Replace with actual URL
    },
 "severe bleeding": {
        "description": """
*Recognizing Severe Bleeding:*
- Blood is flowing out rapidly or spurting.
- The wound is large or deep.
- The person feels dizzy, lightheaded, or weak.

*What to Do:*
1. *Call Emergency Services Immediately:*
   - Provide details about the location and severity of the bleeding.
2. *Apply Direct Pressure to the Wound:*
   - Use a clean cloth or bandage and press firmly to control bleeding.
3. *Elevate the Injured Area (if possible):*
   - Raise the limb above the level of the heart to reduce blood flow to the area.
4. *Use a Tourniquet (only if necessary and trained to do so):*
   - Apply above the wound if bleeding cannot be controlled with direct pressure.
5. *Avoid Removing Objects:*
   - If an object is embedded in the wound, do not remove it. Stabilize the object and cover the wound.
6. *Keep the Person Warm and Calm:*
   - Use blankets to prevent shock and provide reassurance.

*Aftercare:*
- Continue applying pressure until help arrives.
- Monitor the person’s vital signs and consciousness level.
        """,
        "image": "https://www.cleveland.com/resizer/v2/https%3A%2F%2Fadvancelocal-adapter-image-uploads.s3.amazonaws.com%2Fexpo.advance.net%2Fimg%2F85e8de8fc8%2Fwidth2048%2Fc52_stopthebleedposter57e2de68c2f1d.jpeg?auth=7ff23b78bfa1dc870ce9a492b96195481e811f885284fd33a3f7475b32404b88&width=1280&quality=90"
    },
    "breathing issues": {
        "description": """
*Recognizing Breathing Issues:*
- Difficulty breathing or shortness of breath.
- Wheezing or gasping for air.
- Bluish lips or face.
- Struggling to speak full sentences.

*What to Do:*
1. *Call Emergency Services Immediately:*
   - Describe the symptoms and your location.
2. *Ensure an Open Airway:*
   - Position the person sitting upright to make breathing easier.
3. *Administer Rescue Breathing or CPR (if trained and necessary):*
   - For rescue breathing, tilt the person’s head back, lift the chin, and give breaths.
4. *Use an EpiPen for Severe Allergic Reactions (if available and trained):*
   - Inject into the outer thigh and follow up with emergency services.
5. *Avoid Giving Food or Drink:*
   - Prevent choking hazards if the person has difficulty swallowing.
6. *Stay Calm and Reassure the Person:*
   - Encourage slow, deep breaths and provide comfort.

*Aftercare:*
- Continue monitoring the person’s breathing and responsiveness until help arrives.
        """,
        "image": "https://cdn.medizzy.com/RTukU1lxpCGgaQAHVISDYaDArs8=/680x680/img/posts/dfc3ede7-ffee-47e3-83ed-e7ffeeb7e3bb"
    },
    "shock": {
        "description": """
*Recognizing Shock:*
- Pale, cool, and clammy skin.
- Rapid, weak pulse.
- Rapid breathing.
- Dizziness or fainting.
- Weakness or fatigue.
- Nausea or vomiting.

*What to Do:*
1. *Call Emergency Services Immediately:*
   - Provide information about the situation and symptoms.
2. *Lay the Person Down and Elevate Their Legs:*
   - If possible, to improve blood flow to vital organs.
3. *Keep the Person Warm:*
   - Use blankets to maintain body temperature and prevent hypothermia.
4. *Do Not Give Food or Drink:*
   - Avoid complications like choking or vomiting.
5. *Monitor Vital Signs:*
   - Keep track of pulse, breathing, and consciousness.
6. *Provide Reassurance and Comfort:*
   - Help the person stay calm and avoid unnecessary movement.

*Aftercare:*
- Continue monitoring the person’s condition until emergency responders arrive.
- If the person becomes unconscious, ensure they are breathing and begin CPR if necessary.
        """,
        "image": "https://hsseworld.com/wp-content/uploads/2021/03/Electrical-Shock-Survival.png"
    },
    "burns": {
        "description": """
*Recognizing Burns:*
- *First-Degree Burns:* Red, painful, no blisters.
- *Second-Degree Burns:* Red, blistered, swollen, and painful.
- *Third-Degree Burns:* White or charred skin, numbness due to nerve damage.

*What to Do:*
1. *Assess the Severity of the Burn:*
   - Determine if it’s first, second, or third-degree.
2. *Call Emergency Services for Severe Burns:*
   - Third-degree burns or large second-degree burns require immediate medical attention.
3. *Cool the Burn:*
   - Hold the burned area under cool (not cold) running water for at least 10-20 minutes.
   - Alternatively, apply a cool, wet compress if running water is unavailable.
4. *Remove Tight Items:*
   - Take off rings, bracelets, or any constrictive clothing near the burn site.
5. *Cover the Burn:*
   - Use a sterile, non-stick bandage or clean cloth to cover the area.
6. *Avoid Using Ice, Greasy Substances, or Adhesive Bandages:*
   - These can cause further damage or infection.
7. *Do Not Break Blisters:*
   - Protect blisters as they help prevent infection.

*Aftercare:*
- Monitor for signs of infection, such as increased redness, swelling, or pus.
- Keep the burn clean and dry.
- Seek professional medical care for burns covering large areas or involving critical parts of the body.
        """,
        "image": "https://img.freepik.com/premium-vector/skin-burn-stages-infographics-treatment-thermal-burns-types-burning-hands-medical-care-safety-fire-body-skin-first-aid-injury-recent-vector-poster_543062-5541.jpg?w=740"
    },
    "fractures": {
        "description": """
*Recognizing Fractures:*
- Intense pain at the injury site.
- Swelling and bruising.
- Deformity or unnatural positioning of the limb.
- Inability to move the affected area.
- Grinding or snapping sound at the time of injury.

*What to Do:*
1. *Call Emergency Services Immediately for Severe Fractures:*
   - Especially if the bone is protruding through the skin or if it’s a suspected spinal injury.
2. *Immobilize the Area:*
   - Use a splint or a makeshift support (e.g., sticks, rolled newspapers) to keep the limb from moving.
3. *Apply a Cold Pack:*
   - Reduce swelling and pain by applying ice wrapped in a cloth to the injured area for 15-20 minutes.
4. *Elevate the Injured Limb:*
   - Raise the limb above heart level to reduce swelling, if possible and without causing further harm.
5. *Control Bleeding (if present):*
   - Apply gentle pressure with a clean cloth or bandage.
6. *Provide Comfort and Reassure the Person:*
   - Keep them calm and still to prevent further injury.

*Aftercare:*
- Do not attempt to realign the bone.
- Keep the person warm and monitor their condition until help arrives.
- Avoid giving food or drink if surgery is needed.
        """,
        "image": "https://c8.alamy.com/comp/HYR6XY/green-background-vector-illustration-of-a-leg-bandage-HYR6XY.jpg"
    },
    
    
    "poisoning": {
        "description": """
*Recognizing Poisoning:*
- *Ingestion:*
  - Nausea, vomiting, abdominal pain.
  - Confusion, dizziness, or drowsiness.
  - Difficulty breathing or irregular heartbeat.

- *Inhalation:*
  - Coughing, wheezing, or difficulty breathing.
  - Chest tightness or pain.

- *Skin Contact:*
  - Redness, irritation, or burns.
  - Pain or swelling at the contact site.

*What to Do:*
1. *Identify the Poison:*
   - Determine what substance was ingested, inhaled, or contacted.
2. *Call Emergency Services Immediately:*
   - Provide details about the poison, quantity, and time of exposure.
3. *If Ingested:*
   - *Do Not Induce Vomiting Unless Instructed:*
     - Some poisons can cause more damage if vomited.
   - *Provide Information to Poison Control:*
     - If available, contact a poison control center for specific instructions.
4. *If Inhaled:*
   - Move the person to fresh air immediately.
   - Loosen any tight clothing and ensure they are breathing comfortably.
5. *If in Contact with Skin:*
   - Remove contaminated clothing.
   - Rinse the affected area with plenty of water for at least 15 minutes.
6. *Monitor the Person’s Vital Signs:*
   - Check breathing, pulse, and level of consciousness.
7. *Provide Supportive Care:*
   - Keep the person calm and comfortable.
   - Prevent choking or aspiration if the person is unconscious.

*Aftercare:*
- Continue to monitor the person’s condition until medical help arrives.
- If instructed by poison control or medical professionals, follow their guidance for further actions.
        """,
        "image": "https://image.slidesharecdn.com/awarenessprogrameng2-160830064800/85/FIRST-AID-MEASURES-IN-POISONING-5-320.jpg"
    },
    # Add more medical emergencies as needed
}



# Non-medical emergency data with URLs
non_medical_emergency_data = {
    "earthquake": {
        "description": """Steps to follow during an earthquake:
1. Drop to your hands and knees to prevent falling.
2. Take cover under sturdy furniture, such as a table or desk. Protect your head and neck with your arms if no shelter is available.
3. Hold on to your shelter or position until the shaking stops.
4. Stay away from windows, outside walls, and doorways.
5. If outdoors, move to an open area, avoiding buildings, trees, streetlights, and utility wires.""",
        "image": "https://www.earthquakecountry.org/library/EarthquakeProtectiveActionAccessibilityPostcard-EN.png"  # Replace with actual URL
    },
    "tsunami": {
        "description": """Steps to follow during a tsunami:
1. Move to higher ground or as far inland as possible immediately.
2. Do not wait for an official warning if you feel strong shaking near the coast.
3. Avoid rivers, streams, and low-lying areas leading to the ocean.
4. Listen to emergency broadcasts for updates and instructions.
5. Stay in a safe location until authorities declare it safe to return.
6. Stay away from the beach, as tsunamis may come in multiple waves.""",
        "image": "https://uwiseismic.com/wp-content/uploads/2021/04/19.png"  # Replace with actual URL
    },
"flood": {
        "description": """Steps to follow during a flood:
1. Move to higher ground immediately.
2. Avoid walking, swimming, or driving through floodwaters, which can be deceptively dangerous.
3. Disconnect electrical appliances if it’s safe and avoid contact with electrically charged water.
4. If trapped indoors, move to the highest level but avoid closed attics that could trap you.
5. Seek access to the roof if evacuation may be necessary for rescue.""",
        "image": "https://hsseworld.com/wp-content/uploads/2022/02/Flood-safety-Tips-752x1024.png"
    },
    "fire": {
        "description": """Steps to follow during a fire:
1. Evacuate immediately, using stairs instead of elevators.
2. Stay low to the ground if there is smoke, crawling if needed to minimize inhalation.
3. Cover your nose and mouth with a cloth, ideally damp, to filter out smoke.
4. If trapped, go to a window and signal for help with a cloth or flashlight.
5. Seal doors and air gaps with towels or clothing to keep smoke out until help arrives.""",
        "image": "https://www.oneeducation.org.uk/wp-content/uploads/2021/03/Fire-action-signs-768x621.jpg"
    },
    "accident": {
        "description": """Steps to follow during an accident:
1. Call emergency services immediately.
2. Ensure the scene is safe before approaching or helping others.
3. Do not move any injured person unless there is immediate danger.
4. Apply pressure to bleeding wounds to control bleeding.
5. Check for consciousness and breathing. If trained, perform CPR if necessary.
6. Stay with the injured person and keep them calm until help arrives.""",
        "image": "https://img.freepik.com/free-vector/road-accidents-infographic-set_1284-15383.jpg?w=360"
    },
    # Add more non-medical emergencies here
}


# Function to display emergency instructions and image with TTS
def display_emergency_info(emergency_type, emergency_data):
    st.subheader(f"Instructions for {emergency_type.capitalize()}:")
    st.write(emergency_data["description"])
    
    # Load image from URL
    response = requests.get(emergency_data["image"])
    img = Image.open(BytesIO(response.content))
    st.image(img, use_column_width=True)

    # Text-to-speech for reading instructions
    tts = gTTS(text=emergency_data["description"], lang='en')
    with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as temp_audio:
        tts.save(temp_audio.name)
        st.audio(temp_audio.name, format="audio/mp3")

# Main Menu: Choose between Medical and Non-Medical Emergencies
def main_menu():
    st.header("Select an Emergency Category:")
    col1, col2 = st.columns(2)
    with col1:
        if st.button("Medical Emergencies"):
            st.session_state.page = "medical"
            st.rerun()

    with col2:
        if st.button("Non-Medical Emergencies"):
            st.session_state.page = "non-medical"
            st.rerun()
# Medical Emergencies Menu
def medical_menu():
    st.header("Medical Emergencies")
    for emergency in medical_emergency_data:
        if st.button(emergency.capitalize()):
            st.session_state.selected_emergency = emergency
            st.session_state.page = "emergency_info"
            st.session_state.category = "medical"
            st.rerun()
    if st.button("Back to Main Menu"):
        st.session_state.page = "main"
        st.rerun()
# Non-Medical Emergencies Menu
def non_medical_menu():
    st.header("Non-Medical Emergencies")
    for emergency in non_medical_emergency_data:
        if st.button(emergency.capitalize()):
            st.session_state.selected_emergency = emergency
            st.session_state.page = "emergency_info"
            st.session_state.category = "non-medical"
            st.rerun()
    if st.button("Back to Main Menu"):
        st.session_state.page = "main"
        st.rerun()


# Embed JavaScript for voice recognition in the browser
def speech_recognition_ui():
    st.write("""
    <html>
        <body>
            <button onclick="startDictation()">Start Voice Command</button>
            <input type="text" id="transcript" placeholder="Working on it soonnn..." size="50">
            <script>
                function startDictation() {
                    if (window.hasOwnProperty('webkitSpeechRecognition')) {
                        var recognition = new webkitSpeechRecognition();
                        recognition.continuous = false;
                        recognition.interimResults = false;
                        recognition.lang = "en-US";
                        recognition.start();
                        
                        recognition.onresult = function(e) {
                            document.getElementById('transcript').value = e.results[0][0].transcript;
                            document.getElementById('transcript').dispatchEvent(new Event('change'));
                            recognition.stop();
                        };
                        
                        recognition.onerror = function(e) {
                            recognition.stop();
                        };
                    }
                }
            </script>
        </body>
    </html>
    """, unsafe_allow_html=True)


# Text input to receive voice recognition results
voice_command = voice_command = st.text_input("Type Here Looking For:")


# Main logic based on session state
if 'page' not in st.session_state:
    st.session_state.page = "main"
if 'selected_emergency' not in st.session_state:
    st.session_state.selected_emergency = None
if 'category' not in st.session_state:
    st.session_state.category = None

# Display the voice recognition UI
st.text("Working on it soon in new update:")
speech_recognition_ui()
# Page control
if st.session_state.page == "main":
    main_menu()
elif st.session_state.page == "medical":
    medical_menu()
elif st.session_state.page == "non-medical":
    non_medical_menu()
elif st.session_state.page == "emergency_info":
    if st.session_state.category == "medical":
        display_emergency_info(st.session_state.selected_emergency, medical_emergency_data[st.session_state.selected_emergency])
    elif st.session_state.category == "non-medical":
        display_emergency_info(st.session_state.selected_emergency, non_medical_emergency_data[st.session_state.selected_emergency])
    if st.button("Back"):
        st.session_state.page = f"{st.session_state.category}"
        st.rerun()
# JSON data containing emergency numbers
data = [
    {"Country": "USA", "Police Number": "911", "Fire Number": "911", "Ambulance Number": "911"},
    {"Country": "UK", "Police Number": "999", "Fire Number": "999", "Ambulance Number": "999"},
    {"Country": "Canada", "Police Number": "911", "Fire Number": "911", "Ambulance Number": "911"},
    {"Country": "India", "Police Number": "100", "Fire Number": "101", "Ambulance Number": "102"},
    {"Country": "Pakistan", "Police Number": "15", "Fire Number": "16", "Ambulance Number": "115"},
    {"Country": "Australia", "Police Number": "000", "Fire Number": "000", "Ambulance Number": "000"},
    {"Country": "Germany", "Police Number": "110", "Fire Number": "112", "Ambulance Number": "112"},
    {"Country": "France", "Police Number": "17", "Fire Number": "18", "Ambulance Number": "15"},
    {"Country": "Italy", "Police Number": "112", "Fire Number": "115", "Ambulance Number": "118"},
    {"Country": "Spain", "Police Number": "112", "Fire Number": "112", "Ambulance Number": "112"},
    {"Country": "South Africa", "Police Number": "10111", "Fire Number": "10177", "Ambulance Number": "10177"},
    {"Country": "Brazil", "Police Number": "190", "Fire Number": "193", "Ambulance Number": "192"},
    {"Country": "Mexico", "Police Number": "911", "Fire Number": "911", "Ambulance Number": "911"},
    {"Country": "Russia", "Police Number": "102", "Fire Number": "101", "Ambulance Number": "103"},
    {"Country": "China", "Police Number": "110", "Fire Number": "119", "Ambulance Number": "120"},
    {"Country": "Japan", "Police Number": "110", "Fire Number": "119", "Ambulance Number": "119"},
    {"Country": "South Korea", "Police Number": "112", "Fire Number": "119", "Ambulance Number": "119"},
    {"Country": "New Zealand", "Police Number": "111", "Fire Number": "111", "Ambulance Number": "111"},
    {"Country": "Egypt", "Police Number": "122", "Fire Number": "180", "Ambulance Number": "123"},
    {"Country": "Saudi Arabia", "Police Number": "999", "Fire Number": "998", "Ambulance Number": "997"},
    {"Country": "United Arab Emirates", "Police Number": "999", "Fire Number": "997", "Ambulance Number": "998"},
    {"Country": "Argentina", "Police Number": "101", "Fire Number": "100", "Ambulance Number": "107"},
    {"Country": "Chile", "Police Number": "133", "Fire Number": "132", "Ambulance Number": "131"},
    {"Country": "Turkey", "Police Number": "155", "Fire Number": "110", "Ambulance Number": "112"},
    {"Country": "Indonesia", "Police Number": "110", "Fire Number": "113", "Ambulance Number": "118"},
    {"Country": "Thailand", "Police Number": "191", "Fire Number": "199", "Ambulance Number": "1669"},
    {"Country": "Vietnam", "Police Number": "113", "Fire Number": "114", "Ambulance Number": "115"},
    {"Country": "Colombia", "Police Number": "123", "Fire Number": "123", "Ambulance Number": "123"},
    {"Country": "Nigeria", "Police Number": "112", "Fire Number": "112", "Ambulance Number": "112"},
    {"Country": "Bangladesh", "Police Number": "999", "Fire Number": "199", "Ambulance Number": "199"},
    {"Country": "Ukraine", "Police Number": "102", "Fire Number": "101", "Ambulance Number": "103"},
    {"Country": "Poland", "Police Number": "997", "Fire Number": "998", "Ambulance Number": "999"},
    {"Country": "Romania", "Police Number": "112", "Fire Number": "112", "Ambulance Number": "112"},
    {"Country": "Belgium", "Police Number": "101", "Fire Number": "100", "Ambulance Number": "100"},
    {"Country": "Portugal", "Police Number": "112", "Fire Number": "112", "Ambulance Number": "112"},
    {"Country": "Netherlands", "Police Number": "112", "Fire Number": "112", "Ambulance Number": "112"},
    {"Country": "Czech Republic", "Police Number": "112", "Fire Number": "112", "Ambulance Number": "112"},
    {"Country": "Greece", "Police Number": "100", "Fire Number": "199", "Ambulance Number": "166"},
    {"Country": "Switzerland", "Police Number": "117", "Fire Number": "118", "Ambulance Number": "144"},
    {"Country": "Norway", "Police Number": "112", "Fire Number": "110", "Ambulance Number": "113"},
    {"Country": "Sweden", "Police Number": "112", "Fire Number": "112", "Ambulance Number": "112"},
    {"Country": "Finland", "Police Number": "112", "Fire Number": "112", "Ambulance Number": "112"},
    {"Country": "Denmark", "Police Number": "112", "Fire Number": "112", "Ambulance Number": "112"},
    {"Country": "Ireland", "Police Number": "112", "Fire Number": "112", "Ambulance Number": "112"},
    {"Country": "Hungary", "Police Number": "112", "Fire Number": "112", "Ambulance Number": "112"},
    {"Country": "Slovakia", "Police Number": "112", "Fire Number": "112", "Ambulance Number": "112"},
    {"Country": "Bulgaria", "Police Number": "112", "Fire Number": "112", "Ambulance Number": "112"},
    {"Country": "Croatia", "Police Number": "112", "Fire Number": "112", "Ambulance Number": "112"},
    {"Country": "Serbia", "Police Number": "112", "Fire Number": "112", "Ambulance Number": "112"},
    {"Country": "Bosnia and Herzegovina", "Police Number": "122", "Fire Number": "123", "Ambulance Number": "124"},
    {"Country": "Montenegro", "Police Number": "112", "Fire Number": "112", "Ambulance Number": "112"},
    {"Country": "Kosovo", "Police Number": "112", "Fire Number": "112", "Ambulance Number": "112"},
    {"Country": "Albania", "Police Number": "129", "Fire Number": "128", "Ambulance Number": "127"},
    {"Country": "Macedonia", "Police Number": "192", "Fire Number": "193", "Ambulance Number": "194"},
    {"Country": "Malta", "Police Number": "112", "Fire Number": "112", "Ambulance Number": "112"},
    {"Country": "Luxembourg", "Police Number": "113", "Fire Number": "112", "Ambulance Number": "112"},
    {"Country": "Monaco", "Police Number": "17", "Fire Number": "18", "Ambulance Number": "18"},
    {"Country": "Liechtenstein", "Police Number": "112", "Fire Number": "112", "Ambulance Number": "112"},
    {"Country": "San Marino", "Police Number": "112", "Fire Number": "115", "Ambulance Number": "118"},
    {"Country": "Andorra", "Police Number": "112", "Fire Number": "112", "Ambulance Number": "112"},
    {"Country": "Armenia", "Police Number": "102", "Fire Number": "101", "Ambulance Number": "103"},
    {"Country": "Georgia", "Police Number": "112", "Fire Number": "112", "Ambulance Number": "112"},
    {"Country": "Azerbaijan", "Police Number": "102", "Fire Number": "101", "Ambulance Number": "103"},
    {"Country": "Kazakhstan", "Police Number": "102", "Fire Number": "101", "Ambulance Number": "103"},
    {"Country": "Turkmenistan", "Police Number": "102", "Fire Number": "101", "Ambulance Number": "103"},
    {"Country": "Tajikistan", "Police Number": "102", "Fire Number": "101", "Ambulance Number": "103"},
]

# Convert data into a dictionary for quick access
country_data = {entry['Country']: entry for entry in data}

# Create a list of country names for the dropdown
country_list = [entry['Country'] for entry in data]

# Streamlit function to display emergency numbers based on selected country
def display_emergency_numbers(country):
    country = country.strip().title()  # Clean and format the input
    if country in country_data:
        numbers = country_data[country]
        st.write(f"### Emergency Numbers for {numbers['Country']}")
        st.write(f"**Police Number**: {numbers['Police Number']}")
        st.write(f"**Fire Number**: {numbers['Fire Number']}")
        st.write(f"**Ambulance Number**: {numbers['Ambulance Number']}")
    else:
        st.write("Sorry, we don't have data for this country.")

# Streamlit interface
st.subheader("Emergency Numbers by Country")
st.write(
    "Select a country from the dropdown to get the emergency numbers (Police, Fire, Ambulance)."
)

# Add a selectbox for country selection
country_input = st.selectbox("Choose a Country:", country_list)

# Button to trigger the search
if st.button("Get Emergency Numbers"):
    display_emergency_numbers(country_input)

# Optional: Add styling to improve UI
st.markdown("""
<style>
    .css-1v0mbdj {
        background-color: #f0f8ff;
    }
    .css-ffhzg2 {
        color: #00008b;
    }
    .stTextInput input {
        font-size: 18px;
    }
</style>
""", unsafe_allow_html=True)    


# Your main app code goes here

# Add the team name at the bottom left
st.markdown(
    """
    <style>
    .footer {
        position: fixed;
        left: 0;
        bottom: 0;
        width: 100%;
        background-color: transparent;
        color: gray;
        text-align: left;
        padding: 10px;
        font-size: medium;
        font-weight: bold;
    }
    </style>
    <div class="footer">
        Presented by F&F developers
    </div>
    """,
    unsafe_allow_html=True
)

    
