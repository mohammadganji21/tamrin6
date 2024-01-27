def process_emails_and_print_domains():
    num_of_emails = get_number_of_emails_to_process()
    unique_domains = extract_unique_domains(num_of_emails)
    print_sorted_domains(unique_domains)

def get_number_of_emails_to_process():
    return int(input())

def extract_unique_domains(num_of_emails):
    unique_domains = {}
    for _ in range(num_of_emails):
        email = input().strip()
        if check_valid_email(email):
            domain = get_domain_from_email(email)
            unique_domains[domain] = 1
    return unique_domains

def check_valid_email(email):
    return '@' in email and '.' in email.split('@')[-1]

def get_domain_from_email(email):
    return email.split('@')[-1]

def print_sorted_domains(domains):
    sorted_domains = sort_domains(domains)
    display_domains(sorted_domains)

def sort_domains(domains):
    return sorted(domains.keys())

def display_domains(domains):
    for domain in domains:
        print(domain)

# Let's call the processed emails and domain printing function
process_emails_and_print_domains()
