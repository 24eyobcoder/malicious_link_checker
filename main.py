
from is_valid_url import is_valid_url
from check_url_reachablity import check_url_reachablity
from domain_info import resolve_dns
from domain_info import get_domain_info
from check_phish_tank import check_phishtank_url
from scan_content import scan_content
from ai_checker import check_url_with_chatgpt

def main():
    url=input("Enter a URL: ").strip()
    domain=input("Enter domain like (Google.com)")

    while True:
        print("Choose an option:")
        print("1. Check URL validity")
        print("2. Check URL with AI")

        choice = input("chosee an option (1 or 2): ").strip()

        if choice == '1':
            #check weather the link is valid or not
           if not is_valid_url(url):
                  print("Invalid URL format.")
        
             #function that check reachablity
           if check_url_reachablity(url):
                print(f"The URL {url} is reachable.")
           else:
              print(f"The URL {url} is not reachable.")
    
             #to check domain info and also to resolve dns issue
              get_domain_info(url)
              resolve_dns(domain)
              #to check phishing tank
              check_phishtank_url(url)
              #scan content
              scan_content(url)
        
        elif choice == '2':
            #check url with AI
            result = check_url_with_chatgpt(url)
            print("AI Analysis Result:")
            print(result)

   

    
if __name__ == "__main__":
    main()
# This code imports the functions from the two modules and uses them to check if a URL is valid and reachable.
# The user is prompted to enter a URL, and the program checks its validity and reachability, printing the appropriate messages.
# The code is structured to be run as a script, with the main function being called when the script is executed directly.


    