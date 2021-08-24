
def previewParagraphs(s, nchar=50):
  lines = s.splitlines();
  for i, line in enumerate(lines):
    continuation = ""
    if len(line) > nchar:
      continuation = " ..."
    print(f"-- { i+1 }: { line[:nchar] }{ continuation }")
