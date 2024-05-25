def scrape_transactions(url):
    try:
        # Send a GET request to the URL
        response = requests.get(url)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Parse the HTML content of the page
            soup = BeautifulSoup(response.content, "html.parser")

            # Find the table containing the transactions data with a specific class
            table = soup.find("table", class_="mantine-Table-root w-full min-w-max rounded-lg undefined mantine-1mitp60 mantine-Table-scrollable")

            # Check if the table is found
            if table:
                # Read the table into a pandas DataFrame
                df = pd.read_html(str(table), header=0)[0]

                # Save the DataFrame to an Excel file
                df.to_excel("transactions_data.xlsx", index=False)

                print("Data saved to 'transactions_data.xlsx'")
            else:
                print("Table not found on the page.")

        else:
            print("Failed to retrieve data from the website.")

    except Exception as e:
        print("An error occurred:", e)