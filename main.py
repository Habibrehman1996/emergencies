import streamlit as st
from PIL import Image
from gtts import gTTS
import requests
import tempfile
from io import BytesIO

# Title of the app
st.title('Emergency Help - Voice Assisted')

# Introduction to the app
st.write("""
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
        "image": "https://example.com/images/heart_attack.jpg"  # Replace with actual URL
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
        "image": "https://example.com/images/stroke.jpg"  # Replace with actual URL
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
        "image": "images/severe_bleeding.jpg"
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
        "image": "images/breathing_issues.jpg"
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
        "image": "images/shock.jpg"
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
        "image": "images/burns.jpg"
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
        "image": "images/fractures.jpg"
    },
    "head injury": {
        "description": """
*Recognizing a Head Injury:*
- Loss of consciousness, even briefly.
- Dizziness, confusion, or disorientation.
- Headache, nausea, or vomiting.
- Blurred vision or ringing in the ears.
- Slurred speech or difficulty speaking.
- Uneven pupil size or difficulty maintaining balance.

*What to Do:*
1. *Call Emergency Services Immediately for Severe Head Injuries:*
   - Especially if the person is unconscious, has severe bleeding, or shows signs of a concussion.
2. *Do Not Move the Person if a Spinal Injury is Suspected:*
   - Keep the head, neck, and spine aligned and immobile.
3. *Monitor the Person’s Vital Signs:*
   - Check for breathing, pulse, and level of consciousness.
4. *Apply a Cold Pack to Reduce Swelling:*
   - Place ice wrapped in a cloth on the injured area for 15-20 minutes.
5. *Keep the Person Still and Calm:*
   - Limit movement to prevent further injury.
6. *Do Not Give Food or Drink:*
   - Avoid potential complications if surgery is required.
7. *If the Person is Vomiting or Unconscious, Place Them in the Recovery Position:*
   - This helps keep the airway clear and reduces the risk of choking.

*Aftercare:*
- Continue monitoring the person until emergency responders arrive.
- Seek professional medical evaluation, even if the injury seems minor, to rule out internal damage.
        """,
        "image": "images/head_injury.jpg"
    },
    "allergic reaction": {
        "description": """
*Recognizing an Allergic Reaction:*
- *Mild Symptoms:*
  - Itchy skin, rash, or hives.
  - Sneezing, runny nose, or itchy eyes.

- *Severe Symptoms (Anaphylaxis):*
  - Difficulty breathing or swallowing.
  - Swelling of the face, lips, tongue, or throat.
  - Rapid or weak pulse.
  - Dizziness or fainting.
  - Nausea, vomiting, or diarrhea.
  - Tightness in the chest or throat.

*What to Do:*
1. *Assess the Severity of the Reaction:*
   - Identify if it's a mild allergic reaction or anaphylaxis.
2. *For Mild Reactions:*
   - Administer an antihistamine if available and appropriate.
   - Remove the allergen if possible (e.g., take away peanuts, move away from a bee sting).
   - Apply soothing lotions or creams for skin rashes.
3. *For Severe Reactions (Anaphylaxis):*
   - *Use an EpiPen (if available and trained):*
     - Inject into the outer thigh, even through clothing.
   - *Call Emergency Services Immediately:*
     - Inform them of the anaphylactic reaction and any administered medications.
   - *Begin CPR if the Person Becomes Unconscious and is Not Breathing:*
     - Follow standard CPR procedures.
4. *Keep the Person Calm and Still:*
   - Reduce movement to prevent worsening of symptoms.
5. *Monitor Vital Signs:*
   - Keep track of breathing, pulse, and consciousness level.
6. *Avoid Giving Food or Drink:*
   - Prevent choking, especially if the person is having difficulty swallowing.

*Aftercare:*
- Stay with the person until medical help arrives.
- If an EpiPen was used, follow up with additional doses if symptoms persist and until emergency responders take over.
        """,
        "image": "images/allergic_reaction.jpg"
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
        "image": "images/poisoning.jpg"
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
        "image": "https://www.shutterstock.com/image-vector/earthquake-safety-rules-instruction-vector-260nw-2348736933.jpg"  # Replace with actual URL
    },
    "tsunami": {
        "description": """Steps to follow during a tsunami:
1. Move to higher ground or as far inland as possible immediately.
2. Do not wait for an official warning if you feel strong shaking near the coast.
3. Avoid rivers, streams, and low-lying areas leading to the ocean.
4. Listen to emergency broadcasts for updates and instructions.
5. Stay in a safe location until authorities declare it safe to return.
6. Stay away from the beach, as tsunamis may come in multiple waves.""",
        "image": "https://example.com/images/tsunami.jpg"  # Replace with actual URL
    },
"flood": {
        "description": """Steps to follow during a flood:
1. Move to higher ground immediately.
2. Avoid walking, swimming, or driving through floodwaters, which can be deceptively dangerous.
3. Disconnect electrical appliances if it’s safe and avoid contact with electrically charged water.
4. If trapped indoors, move to the highest level but avoid closed attics that could trap you.
5. Seek access to the roof if evacuation may be necessary for rescue.""",
        "image": "images/flood.jpg"
    },
    "fire": {
        "description": """Steps to follow during a fire:
1. Evacuate immediately, using stairs instead of elevators.
2. Stay low to the ground if there is smoke, crawling if needed to minimize inhalation.
3. Cover your nose and mouth with a cloth, ideally damp, to filter out smoke.
4. If trapped, go to a window and signal for help with a cloth or flashlight.
5. Seal doors and air gaps with towels or clothing to keep smoke out until help arrives.""",
        "image": "images/fire.jpg"
    },
    "accident": {
        "description": """Steps to follow during an accident:
1. Call emergency services immediately.
2. Ensure the scene is safe before approaching or helping others.
3. Do not move any injured person unless there is immediate danger.
4. Apply pressure to bleeding wounds to control bleeding.
5. Check for consciousness and breathing. If trained, perform CPR if necessary.
6. Stay with the injured person and keep them calm until help arrives.""",
        "image": "https://www.shutterstock.com/shutterstock/photos/1234348078/display_1500/stock-vector-what-to-do-after-car-accident-instruction-call-and-wait-for-police-automobile-damage-and-tow-1234348078.jpg"
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

    with col2:
        if st.button("Non-Medical Emergencies"):
            st.session_state.page = "non-medical"

# Medical Emergencies Menu
def medical_menu():
    st.header("Medical Emergencies")
    for emergency in medical_emergency_data:
        if st.button(emergency.capitalize()):
            st.session_state.selected_emergency = emergency
            st.session_state.page = "emergency_info"
            st.session_state.category = "medical"
    
    if st.button("Back to Main Menu"):
        st.session_state.page = "main"

# Non-Medical Emergencies Menu
def non_medical_menu():
    st.header("Non-Medical Emergencies")
    for emergency in non_medical_emergency_data:
        if st.button(emergency.capitalize()):
            st.session_state.selected_emergency = emergency
            st.session_state.page = "emergency_info"
            st.session_state.category = "non-medical"
    
    if st.button("Back to Main Menu"):
        st.session_state.page = "main"

# Embed JavaScript for voice recognition in the browser
def speech_recognition_ui():
    st.write("""
    <html>
        <body>
            <button onclick="startDictation()">Start Voice Command</button>
            <input type="text" id="transcript" placeholder="Voice command will appear here" size="50">
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

# Display the voice recognition UI
st.subheader("Use the button below to start voice recognition:")
speech_recognition_ui()

# Text input to receive voice recognition results
voice_command = st.text_input("Recognized Command (say 'heart attack', 'stroke', etc.):")

# Process voice commands
if voice_command:
    st.write(f"Voice Command: {voice_command}")
    if voice_command.lower() in medical_emergency_data:
        st.session_state.selected_emergency = voice_command.lower()
        st.session_state.page = "emergency_info"
        st.session_state.category = "medical"
    elif voice_command.lower() in non_medical_emergency_data:
        st.session_state.selected_emergency = voice_command.lower()
        st.session_state.page = "emergency_info"
        st.session_state.category = "non-medical"
    else:
        st.write("Sorry, I didn't recognize the emergency. Please try again.")

# Main logic based on session state
if 'page' not in st.session_state:
    st.session_state.page = "main"
if 'selected_emergency' not in st.session_state:
    st.session_state.selected_emergency = None
if 'category' not in st.session_state:
    st.session_state.category = None

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
