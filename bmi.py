import streamlit as st
from streamlit_option_menu import option_menu
st.title("📇 BMI CALACULATOR")

st.markdown('''
            <style>
            .advice {
            border: 1px solid #4CAF50;
            border-radius: 10px;
            padding: 10px;
            margin-top: 10px;
            }
            </style>
            ''',unsafe_allow_html=True)

w=st.number_input("Enter Weight(in kgs)",step=0.1)

h=st.number_input("Enter Height(in cms)",step=0.1)
bt=st.button("CHECK BMI")

if bt:
    bmi=w/((h/100)**2)
    if bmi<25:
        st.success(f"BMI:{bmi:.2f}")
    if bmi<18.5:
        advice = """
        <div class="advice">
            <h4>🚨 You are underweight.</h4>
            <p><strong>Advice and Prescription:</strong></p>
            <ul>
                <li>Increase your caloric intake with nutritious foods such as nuts, dairy, lean meats, and starchy vegetables.</li>
                <li>Consider strength training exercises to build muscle mass.</li>
                <li>Consult with a healthcare provider for personalized advice.</li>
            </ul>
        </div>
        """
    elif 18.5 <=bmi<25:
        advice = """
        <div class="advice">
            <h4>✅ You have a normal weight.</h4>
            <p><strong>Advice and Prescription:</strong></p>
            <ul>
                <li>Maintain a balanced diet rich in fruits, vegetables, whole grains, and lean proteins.</li>
                <li>Continue regular physical activity, aiming for at least 150 minutes of moderate aerobic activity or 75 minutes of vigorous activity per week.</li>
                <li>Regular health check-ups to monitor and maintain your health status.</li>
            </ul>
        </div>
        """
    
    elif 25.1 <= bmi < 29.9:
        st.error(f"BMI:{bmi:.2f}")
        advice = """
        <div class="advice">
            <h4>⚠️ You are overweight.</h4>
            <p><strong>Advice and Prescription:</strong></p>
            <ul>
                <li>Aim for a slow and steady weight loss by reducing caloric intake and increasing physical activity.</li>
                <li>Incorporate more physical activities such as walking, jogging, cycling, or swimming.</li>
                <li>Focus on a diet rich in fiber, such as fruits, vegetables, legumes, and whole grains.</li>
                <li>Consult with a healthcare provider or a nutritionist for a tailored weight loss plan.</li>
            </ul>
        </div>
        """

    else:
        st.error(f"BMI:{bmi:.2f}")
        advice = """
        <div class="advice">
            <h4>🚨 You are obese.</h4>
            <p><strong>Advice and Prescription:</strong></p>
            <ul>
                <li>Seek support from a healthcare provider to create a comprehensive weight loss plan.</li>
                <li>Consider joining a weight loss program for structured guidance and support.</li>
                <li>Increase physical activity gradually, aiming for at least 150 minutes of moderate exercise per week.</li>
                <li>Focus on portion control and reducing high-calorie, low-nutrient foods such as sugary drinks and snacks.</li>
                <li>Regular monitoring of other health indicators such as blood pressure, cholesterol, and blood sugar levels.</li>
            </ul>
        </div>
        """
    
if bt:
    st.markdown(advice,unsafe_allow_html=True)
    tab1,tab2=st.tabs(['DIET PLAN','EXERCISE PLAN'])

    with tab1:
        if bmi<19:
            
            st.info("1. Increase Caloric Intake: Consume more calories than you burn. Focus on nutrient-dense foods.\n2. Protein-Rich Foods: Include lean meats, eggs, dairy products, nuts, and legumes.\n3. Healthy Fats: Avocados, nuts, seeds, and olive oil.\n4. Carbohydrates: Whole grains, fruits, and vegetables.\n5. Frequent Meals: Eat 5-6 small meals throughout the day.")
        if 19< bmi <29.9:
            st.info("1. Balanced Diet: Include a variety of foods from all food groups. \n2. Moderate Portion Sizes: Maintain a calorie balance to keep your weight stable. \n3. Lean Proteins: Chicken, fish, tofu, legumes. n4. Complex Carbs: Whole grains, vegetables, fruits. n5. Healthy Fats: Avocado, nuts, seeds.")

    with tab2:
        if bmi<30:
            st.info("1. Strength Training: Focus on weight lifting and resistance exercises to build muscle mass.\n2. Compound Exercises: Squats, deadlifts, bench presses, and pull-ups.\n3. Low-Intensity Cardio: Walking or light jogging to improve cardiovascular health without excessive calorie burn.")
    





