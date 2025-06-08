import whois
import dns.resolver
import ssl

def get_domain_info(url):
    
    try:
        w = whois.whois(url)
        print("📅 Domain registered:", w.creation_date)
    except:
        print("❌ WHOIS lookup failed.")

def resolve_dns(domain):
    try:
        result = dns.resolver.resolve(domain, 'A')
        print("🧠 DNS resolved successfully:")
        for ip in result:
            print("  🔹", ip.to_text())
    except Exception as e:
        print("❌ DNS resolution failed:", e)
