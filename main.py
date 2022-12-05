import re
content = open('dump.zip','rb').read()

def parse_int(b):
  return int.from_bytes(b,'little')

# Search for End of Central Directory Record
for m in re.finditer(b"PK\5\6", content):
  i = m.start()

  # Parse End of Central Directory Record
  cent_dir_offset= parse_int(content[i+16:i+20])

  # Parse Central Directory Header
  local_header_offset= parse_int(content[cent_dir_offset+42:cent_dir_offset+42+4])

  # Parse Local File Header
  compressed_size = parse_int(content[local_header_offset+18:local_header_offset+22])
  file_name_length = parse_int(content[local_header_offset+26:local_header_offset+28])
  content_start = local_header_offset+30+file_name_length
  comp_content = content[content_start:content_start+compressed_size]
  print(comp_content.decode("ascii"),end="")