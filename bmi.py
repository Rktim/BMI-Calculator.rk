import streamlit as st


def bmi(w,h):
    return w/(h**2)

def main():
    st.title("BMI Calculator .rk")
    weight = st.number_input("Enter your weight (kg):", min_value=00)
    height = st.number_input("Enter your height (m):", min_value=0.0)

    if st.button("Calculate BMI"):
        bmi_value = bmi(weight, height)
        category= None
        if bmi_value < 18.5:
            category = "Underweight"
            message = "It is recommended to gain some weight by eating a healthy and balanced diet."
        elif 18.5 <= bmi_value < 24.9:
            category = "Healthy weight"
            message = "Keep up the good work! Maintain a healthy lifestyle by eating a balanced diet and exercising regularly."
        elif 25.0 <= bmi_value < 29.9:
            category = "Overweight"
            message = "It is recommended to lose some weight by eating a healthy and balanced diet and increasing physical activity."
        else:
            category = "Obesity"
            message = "It is recommended to seek medical advice as obesity can lead to various health issues."


            
        st.success(f"Your BMI: {bmi_value:.2f}")
        st.info(category)
        st.write("->",message)

if __name__ == "__main__":
    main()


#Underweight: Less than 18.5
#Healthy weight: 18.5–24.9
#Overweight: 25.0–29.9
#Obesity: 30.0 or higher 
