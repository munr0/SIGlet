"""
SIGlet - Generate ASCII-art email signatures using FIGlet
"""

import yaml
from pyfiglet import Figlet


def load_profile(yaml_file):
    with open(yaml_file, "r") as f:
        return yaml.safe_load(f)


def generate_ascii_art(name, comma_to_apostrophe=False):
    fig = Figlet(font="big", width=128)
    ascii_art = fig.renderText(name)

    # Optional style override
    if comma_to_apostrophe:
        ascii_art = ascii_art.replace(",", "'")

    return ascii_art, fig.Font.height


def escape_html(text):
    text = text.replace("&", "&amp;")
    text = text.replace("<", "&lt;")
    text = text.replace(">", "&gt;")
    text = text.replace(" ", "&nbsp;")
    return text


def generate_signature_html(profile):

    # Build banner HTML
    ascii_art, height = generate_ascii_art(
        profile["bannername"], profile.get("nocommas", False)
    )
    ascii_lines = ascii_art.rstrip("\n").split("\n")

    skipped = [0, 0]  # [top, bottom]
    while ascii_lines and not ascii_lines[0].strip():
        ascii_lines.pop(0)
        skipped[0] += 1
    while ascii_lines and not ascii_lines[-1].strip():
        ascii_lines.pop()
        skipped[1] += 1

    ascii_html = "<br>".join(escape_html(line) for line in ascii_lines) + "<br>"

    # Build contact info
    padding = [height - skipped[0] - 6, height - skipped[1] - 6]
    contact_html = f"""{'<br>' * padding[0]}
      |&nbsp;&nbsp;{profile['fullname']}<br>
      |&nbsp;&nbsp;{profile['phone']}<br>
      |&nbsp;&nbsp;<a href="mailto:{profile['email']}" target="_blank" style="color:inherit; text-decoration:none;">{profile['email']}</a><br>
      |&nbsp;&nbsp;<a href="https://{profile['website']}" target="_blank" style="color:inherit; text-decoration:none;">{profile['website']}</a><br>
      {'<br>' * padding[1]}<br>"""

    # Build complete HTML
    html = f"""<table cellspacing="0" cellpadding="0" style="font-family: Consolas, monospace; font-size: {profile['font-size']}; line-height: 1; border-collapse: collapse;">
  <tr>
    <td style="vertical-align: top; white-space: nowrap;">
      {ascii_html}
    </td>
    <td style="padding-left: 1em; vertical-align: top; white-space: nowrap;">
      {contact_html}
    </td>
  </tr>
</table>"""

    return html


def main():
    profile = load_profile("profile.yaml")
    html = generate_signature_html(profile)

    output_file = "signature.html"
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(html)

    print(f"Signature generated: {output_file}")


if __name__ == "__main__":
    main()
