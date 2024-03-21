import csv
import re


def csv_to_md(filename):
    """convert Youtrack csv issue export to markdown files

    Args:
        filename: .csv filename
    """
    with open(filename, 'r', encoding='utf-8-sig') as csv_file:

        csv_reader = csv.DictReader(csv_file)

        for i, row in enumerate(csv_reader):

            issue_id = row["Issue Id"]

            with open(f"Requirements/{issue_id}.md", 'w') as md_file:
                md_file.write(f"# {issue_id}\n\n")
                for header, value in row.items():
                    md_file.write(f"## {header}\n")

                    cvalue = re.sub('<.*?>', '', value)
                    fvalue = cvalue.replace('#', '###')
                    md_file.write(f"{fvalue}\n\n")


if __name__ == '__main__':
    csv_to_md('Requirements/Issues.csv')
