import tkinter as tk
from tkinter import messagebox,filedialog
from src.core.dna import *
from src.core.export import save_report

class DNAApp:
    def __init__(self,root):
        self.root=root
        root.title("DNA Analyzer")
        self.text=tk.Text(root,height=6,width=60)
        self.text.pack()
        tk.Button(root,text="Analyze",command=self.analyze).pack()
        tk.Button(root,text="Save Report",command=self.save).pack()
        self.out=tk.Text(root,height=15,width=70)
        self.out.pack()

    def analyze(self):
        try:
            seq=self.text.get("1.0","end").strip()
            report=f"""Length: {length(seq)}
GC%: {calculate_gc(seq)}
Counts: {nucleotide_count(seq)}
RNA: {transcribe_rna(seq)}
Reverse Complement: {reverse_complement(seq)}"""
            self.report=report
            self.out.delete("1.0","end")
            self.out.insert("1.0",report)
        except Exception as e:
            messagebox.showerror("Error",str(e))

    def save(self):
        path=filedialog.asksaveasfilename(defaultextension=".txt")
        if path:
            save_report(path,getattr(self,"report","No report"))
