import streamlit as st
import google.generativeai as genai

GOOGLE_API_KEY = "AIzaSyBVSqa4wKKNhhVV8R-kXEQKWvCXemDJ5Mc"

genai.configure(api_key=GOOGLE_API_KEY)
model=genai.GenerativeModel('gemini-pro')

def main():
    st.set_page_config(page_title="SQL Query Generator" , page_icon=":robot")
    st.markdown(
        """
            <div style ="text-align: center;">
                <h1>SQL Query Generator</h1>
                <h3>I can Generate SQL queries for you!</h3>
                <h4>With Explanation as well !!</h4>
                <p>This tool is a simple tool that allows you to generate SQL Queries based on your prompts</p>
            </div>    

        """,
        unsafe_allow_html=True,

    )
    text_input=st.text_area("Enter your Query here in Plain English")
    
    submit = st.button("Generate SQL query")
    if submit:
        with st.spinner("Generating SQL Query . . ."):
            template="""
                Create a sql query snippet using the below text:
                ```
                    {text_input}
                ```
                i just want a SQL query.
            """
        formatted_template=template.format(text_input=text_input)
        st.write(formatted_template)
        response=model.generate_content(formatted_template)
        sql_query=response.text
        st.write(sql_query)
        expected_output="""
            What would be the expected response of this SQL query snippet:
                ```
                    {sql_query}
                ```
            Provide sample tabular Response with no explanation:
        """
        expected_output_formatted=expected_output.format(sql_query=sql_query)
        eoutput=model.generate_content(expected_output_formatted)
        eoutput=eoutput.text
        st.write(eoutput)
        explanation="""
            Explain this Sql query:
                ```
                    {sql_query}
                ```
            Please provide with simplest of explanation:
            """
        explanation_formatted=explanation.format(sql_query=sql_query)
        explanation=model.generate_content(explanation_formatted)
        explanation=explanation.text
        st.write(explanation)
main()    
