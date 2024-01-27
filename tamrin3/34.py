def process_emails_and_print_domains():
    num_of_emails = get_number_of_emails_to_process()
    unique_domains = extract_unique_domains(num_of_emails)
    print_sorted_domains(unique_domains)

def get_number_of_emails_to_process():
    return int(input())

def extract_unique_domains(num_of_emails):
    unique_domains = set()
    for _ in range(num_of_emails):
        email = input().strip()
        if is_valid_email(email):
            domain = get_domain_from_email(email)
            unique_domains.add(domain)
    return unique_domains

def is_valid_email(email):
    return '@' in email and '.' in email.split('@')[-1]

def get_domain_from_email(email):
    return email.split('@')[-1]

def print_sorted_domains(domains):
    sorted_domains = sorted(domains)
    display_domains(sorted_domains)

def display_domains(domains):
    for domain in domains:
        print(domain)

# Let's call the processed emails and domain printing function
if __name__ == "__main__":
    process_emails_and_print_domains()
