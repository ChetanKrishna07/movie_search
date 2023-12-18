import streamlit as st
import requests

# Define the function to make the API call
def get_movie_data(title):
    # Replace with the actual API endpoint
    url = f"http://localhost:8000/title/{title}"
    res = requests.get(url)
    return res.json()


# Streamlit app
def main():
    st.title("Movie Search")

    movie_title = st.text_input("Enter a movie name")

    if st.button("Search"):
        
        results = get_movie_data(movie_title)
        if results["status"] == "error":
            st.error(results["message"])
        else:
            st.success(f"Found {len(results['data'])} movies")
            # Display results
            for result in results["data"]:
                st.markdown(f"### [{result['title']}]({result['wiki_page']})")
                
                # Dropdown for genre
                with st.expander("Show Genre"):
                    st.write(result['genre'])

                # Dropdown for cast
                with st.expander("Show Cast"):
                    st.write(result['cast'])

if __name__ == "__main__":
    main()
