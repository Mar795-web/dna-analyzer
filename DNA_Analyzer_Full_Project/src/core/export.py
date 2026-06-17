def save_report(path, report):
    with open(path,"w",encoding="utf-8") as f:
        f.write(report)
