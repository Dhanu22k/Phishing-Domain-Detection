
from urllib.parse import urlparse
import urlfuntions as uf


def extract_features(url):
    parsed_url = urlparse(url)
    domain=uf.extract_domain(url)
    time_domain_activation ,time_domain_expiration=uf.get_domain_dates(domain)
    features = {
        'qty_dot_url': url.count('.'),
        'qty_hyphen_url': url.count('-'),
        'qty_underline_url': url.count('_'),
        'qty_slash_url': url.count('/'),
        'qty_questionmark_url': url.count('?'),
        'qty_equal_url': url.count('='),
        'qty_at_url': url.count('@'),
        'qty_and_url': url.count('&'),
        'qty_exclamation_url': url.count('!'),
        'qty_space_url': url.count(' '),
        'qty_tilde_url': url.count('~'),
        'qty_comma_url': url.count(','),
        'qty_plus_url': url.count('+'),
        'qty_asterisk_url': url.count('*'),
        'qty_hashtag_url': url.count('#'),
        'qty_dollar_url': url.count('$'),
        'qty_percent_url': url.count('%'),
        'qty_tld_url': len(parsed_url.netloc.split('.')),
        'length_url': len(url),
        'qty_dot_domain': parsed_url.netloc.count('.'),
        'qty_hyphen_domain': parsed_url.netloc.count('-'),
        'qty_underline_domain': parsed_url.netloc.count('_'),
        'qty_slash_domain': parsed_url.netloc.count('/'),
        'qty_questionmark_domain': parsed_url.netloc.count('?'),
        'qty_equal_domain': parsed_url.netloc.count('='),
        'qty_at_domain': parsed_url.netloc.count('@'),
        'qty_and_domain': parsed_url.netloc.count('&'),
        'qty_exclamation_domain': parsed_url.netloc.count('!'),
        'qty_space_domain': parsed_url.netloc.count(' '),
        'qty_tilde_domain': parsed_url.netloc.count('~'),
        'qty_comma_domain': parsed_url.netloc.count(','),
        'qty_plus_domain': parsed_url.netloc.count('+'),
        'qty_asterisk_domain': parsed_url.netloc.count('*'),
        'qty_hashtag_domain': parsed_url.netloc.count('#'),
        'qty_dollar_domain': parsed_url.netloc.count('$'),
        'qty_percent_domain': parsed_url.netloc.count('%'),
        'qty_vowels_domain': sum(1 for char in parsed_url.netloc if char in 'aeiouAEIOU'),
        'domain_length': len(parsed_url.netloc),
        'domain_in_ip': 1 if parsed_url.netloc.replace('.', '').isdigit() else 0,
        'server_client_domain': 0,  # Placeholder, you can add logic to determine this
        'qty_dot_directory': parsed_url.path.count('.'),
        'qty_hyphen_directory': parsed_url.path.count('-'),
        'qty_underline_directory': parsed_url.path.count('_'),
        'qty_slash_directory': parsed_url.path.count('/'),
        'qty_questionmark_directory': parsed_url.path.count('?'),
        'qty_equal_directory': parsed_url.path.count('='),
        'qty_at_directory': parsed_url.path.count('@'),
        'qty_and_directory': parsed_url.path.count('&'),
        'qty_exclamation_directory': parsed_url.path.count('!'),
        'qty_space_directory': parsed_url.path.count(' '),
        'qty_tilde_directory': parsed_url.path.count('~'),
        'qty_comma_directory': parsed_url.path.count(','),
        'qty_plus_directory': parsed_url.path.count('+'),
        'qty_asterisk_directory': parsed_url.path.count('*'),
        'qty_hashtag_directory': parsed_url.path.count('#'),
        'qty_dollar_directory': parsed_url.path.count('$'),
        'qty_percent_directory': parsed_url.path.count('%'),
        'directory_length': len(parsed_url.path),
        'qty_dot_file': parsed_url.path.split('/')[-1].count('.'),
        'qty_hyphen_file': parsed_url.path.split('/')[-1].count('-'),
        'qty_underline_file': parsed_url.path.split('/')[-1].count('_'),
        'qty_slash_file': parsed_url.path.split('/')[-1].count('/'),
        'qty_questionmark_file': parsed_url.path.split('/')[-1].count('?'),
        'qty_equal_file': parsed_url.path.split('/')[-1].count('='),
        'qty_at_file': parsed_url.path.split('/')[-1].count('@'),
        'qty_and_file': parsed_url.path.split('/')[-1].count('&'),
        'qty_exclamation_file': parsed_url.path.split('/')[-1].count('!'),
        'qty_space_file': parsed_url.path.split('/')[-1].count(' '),
        'qty_tilde_file': parsed_url.path.split('/')[-1].count('~'),
        'qty_comma_file': parsed_url.path.split('/')[-1].count(','),
        'qty_plus_file': parsed_url.path.split('/')[-1].count('+'),
        'qty_asterisk_file': parsed_url.path.split('/')[-1].count('*'),
        'qty_hashtag_file': parsed_url.path.split('/')[-1].count('#'),
        'qty_dollar_file': parsed_url.path.split('/')[-1].count('$'),
        'qty_percent_file': parsed_url.path.split('/')[-1].count('%'),
        'file_length': len(parsed_url.path.split('/')[-1]),
        'qty_dot_params': parsed_url.query.count('.'),
        'qty_hyphen_params': parsed_url.query.count('-'),
        'qty_underline_params': parsed_url.query.count('_'),
        'qty_slash_params': parsed_url.query.count('/'),
        'qty_questionmark_params': parsed_url.query.count('?'),
        'qty_equal_params': parsed_url.query.count('='),
        'qty_at_params': parsed_url.query.count('@'),
        'qty_and_params': parsed_url.query.count('&'),
        'qty_exclamation_params': parsed_url.query.count('!'),
        'qty_space_params': parsed_url.query.count(' '),
        'qty_tilde_params': parsed_url.query.count('~'),
        'qty_comma_params': parsed_url.query.count(','),
        'qty_plus_params': parsed_url.query.count('+'),
        'qty_asterisk_params': parsed_url.query.count('*'),
        'qty_hashtag_params': parsed_url.query.count('#'),
        'qty_dollar_params': parsed_url.query.count('$'),
        'qty_percent_params': parsed_url.query.count('%'),
        'params_length': len(parsed_url.query),
        'tld_present_params': 1 if parsed_url.query.endswith('.com') or parsed_url.query.endswith('.net') else 0,
        # Example condition
        'qty_params': len(parsed_url.query.split('&')),
        'email_in_url': 1 if '@' in url else 0,
        'time_response': uf.get_time_response(url),
        'domain_spf': uf.check_spf_record(domain),
        'asn_ip': uf.get_asn_ip(domain),
        'time_domain_activation': time_domain_activation,  # Placeholder, you can add logic to determine this
        'time_domain_expiration': time_domain_expiration,  # Placeholder, you can add logic to determine this
        'qty_ip_resolved': uf.count_unique_ips(domain),  # Placeholder, you can add logic to determine this
        'qty_nameservers': uf.count_nameservers(domain),  # Placeholder, you can add logic to determine this
        'qty_mx_servers': uf.count_mx_servers(url),  # Placeholder, you can add logic to determine this
        'ttl_hostname': uf.get_ttl(domain),  # Placeholder, you can add logic to determine this
        'tls_ssl_certificate': uf.has_ssl_certificate(domain),  # Placeholder, you can add logic to determine this
        'qty_redirects': uf.count_redirects(url),  # Placeholder, you can add logic to determine this
        'url_google_index': uf.is_url_google_indexed(url),  # Placeholder, you can add logic to determine this
        'domain_google_index': uf.is_url_google_indexed(domain),  # Placeholder, you can add logic to determine this
        'url_shortened': uf.is_url_shortened(url)  # Placeholder, you can add logic to determine this
    }

    return features

