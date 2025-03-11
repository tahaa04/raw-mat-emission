import streamlit as st

def main():
    st.title("Emission Calculator")
    
    # Description
    st.markdown("<small>Emissions happen due to acquiring raw materials like Lead and Sulphur for manufacturing electrochemical cells. Calculate emissions with respect to total sales or money spent.</small>", unsafe_allow_html=True)
    
    # User input for total annual sale of batteries
    total_sale = st.number_input("Enter total annual sale of batteries (in rupees):", min_value=0.0, step=1000.0)
    
    if total_sale > 0:
        # Calculations
        totalBatteries = total_sale / 5000
        leadEmission = totalBatteries * 55 * 0.4
        sulphurEmission = totalBatteries * 4.6 * 0.4
        netEmission = leadEmission + sulphurEmission
        
        # Display results
        st.write(f"### Net emission is {netEmission:.2f} kg of Carbon Dioxide.")
        st.markdown(f"<small>Lead Emission: {leadEmission:.2f} kg CO₂</small>", unsafe_allow_html=True)
        st.markdown(f"<small>Sulphur Emission: {sulphurEmission:.2f} kg CO₂</small>", unsafe_allow_html=True)
    else:
        st.write("Please enter a valid sales value greater than 0.")

if __name__ == "__main__":
    main()
