import streamlit as st
import pandas as pd
from modules.browser import start_browser
from modules.login import linkedin_login
from modules.search import linkedin_search
from modules.scroll import scroll_page
from modules.extractor import result_extractor
from modules.session import save_cookies, load_cookies
import time


st.set_page_config(page_title="LinkedIn Lead Extractor", layout="wide")

st.title("🔍 LinkedIn Lead Extraction Tool")
st.write("Extract LinkedIn profiles based on search keyword")

# --- INPUTS ---
email = st.text_input("LinkedIn Email")
password = st.text_input("LinkedIn Password", type="password")
keyword = st.text_input("Search Keyword")
run_button = st.button("Start Extraction")


if run_button:

    if not email or not password or not keyword:
        st.warning("Please fill all fields.")
    else:

        st.info("Starting browser automation...")

        driver = start_browser()

        logged_in = load_cookies(driver)
        driver.refresh()

        if not logged_in:
            linkedin_login(driver, email, password)
            save_cookies(driver)

        time.sleep(3)

        driver.get(f"https://www.linkedin.com/search/results/people/?keywords={keyword}")

        scroll_page(driver, target_count=20)

        data = result_extractor(driver)

        driver.quit()

        if data:
            df = pd.DataFrame(data)

            st.success(f"Extracted {len(df)} profiles")

            st.dataframe(df)

            # Download buttons
            csv = df.to_csv(index=False).encode("utf-8")
            st.download_button(
                label="Download CSV",
                data=csv,
                file_name="linkedin_leads.csv",
                mime="text/csv"
            )

            excel = df.to_excel("temp.xlsx", index=False)
            with open("temp.xlsx", "rb") as f:
                st.download_button(
                    label="Download Excel",
                    data=f,
                    file_name="linkedin_leads.xlsx"
                )

        else:
            st.error("No profiles extracted.")