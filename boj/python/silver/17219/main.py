import sys
readline = sys.stdin.readline

site_with_password_count, finding_site_count = map(int, readline().split())
site_with_password_dict = dict()
for _ in range(site_with_password_count):
    site, password = readline().rstrip().split()
    site_with_password_dict[site] = password
for _ in range(finding_site_count):
    finding_site = readline().rstrip()
    print(site_with_password_dict[finding_site])