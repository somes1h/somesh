import streamlit as st
def efficiency_of_heat_engine(source_temp, sink_temp):
    efficiency = 1 - (sink_temp / source_temp)
    return efficiency * 100  # Convert to percentage
def coefficient_of_performance(source_temp, sink_temp):
    cop = source_temp / (source_temp - sink_temp)
    return cop

def main():
    st.title("Heat Engine Efficiency & Refrigerator Coefficient of Performance Calculator")

    st.write(" Please note that temperature of (SOURCE) > (SINK)")

    source_temp = st.number_input("Enter source temperature (in Kelvin):", min_value=0.1, step=0.1)
    sink_temp = st.number_input("Enter sink temperature (in Kelvin):", min_value=0.1, step=0.1)

    if st.button("Calculate"):
        st.write("### Heat Engine Efficiency:")
        efficiency = efficiency_of_heat_engine(source_temp, sink_temp)
        st.write(f"The efficiency of the heat engine is {efficiency:.2f}%")

        st.write("### Refrigerator Coefficient of Performance:")
        cop = coefficient_of_performance(source_temp, sink_temp)
        st.write(f"The coefficient of performance of the refrigerator is {cop:.2f}")
if __name__ == "__main__":
    main()