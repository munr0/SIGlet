# SIGlet

Make your email signature stand out with FIGlet text banners!

This tool uses the [**big.flf**](https://www.figlet.org/cgi-bin/fontdb_example.cgi?font=big.flf) FIGfont by Glenn Chappell. Signatures use HTML &lt;table&gt; elements to prevent text wrapping for email client/device compatibility.

## Sample Output
<pre>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;_
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|&nbsp;|
&nbsp;&nbsp;__&nbsp;_|&nbsp;|&nbsp;___&nbsp;_&nbsp;__&nbsp;&nbsp;_&nbsp;__&nbsp;&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;Glenn Chappell
&nbsp;/&nbsp;_`&nbsp;|&nbsp;|/&nbsp;_&nbsp;\&nbsp;'_&nbsp;\|&nbsp;'_&nbsp;\&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;100-555-0100
|&nbsp;(_|&nbsp;|&nbsp;|&nbsp;&nbsp;__/&nbsp;|&nbsp;|&nbsp;|&nbsp;|&nbsp;|&nbsp;|&nbsp;&nbsp;|&nbsp;&nbsp;<a href="mailto:info@figlet.org" target="_blank">info@figlet.org</a>
&nbsp;\__'&nbsp;|_|\___|_|&nbsp;|_|_|&nbsp;|_|&nbsp;&nbsp;|&nbsp;&nbsp;<a href="https://www.figlet.org" target="_blank">www.figlet.org</a>
&nbsp;&nbsp;__/&nbsp;|
&nbsp;|___/
</pre>
*For a proper CSS-rich preview, see `example.html`*

## Usage

1. Edit `profile.yaml` with your contact details:
    ```yaml
    bannername: glenn           # FIGlet-rendered banner text
    fullname: Glenn Chappell
    phone: 100-555-0100
    email: info@figlet.org      # creates a mailto anchor
    website: www.figlet.org     # exclude the URI scheme
    font-size: 11pt             # CSS font size of all signature text
    nocommas: true              # Override FIGlet commas with straight apostrophes
                                  # (for letters a, d, g, q, u, y)
    ```

2. Run the generator
    ```bash
    python siglet.py
    ```

3. Open the generated `signature.html` with a web browser
4. <kbd>Ctrl</kbd> <kbd>A</kbd>, <kbd>Ctrl</kbd> <kbd>C</kbd> the rendered HTML, <kbd>Ctrl</kbd> <kbd>V</kbd> into your email client

## Requirements

```bash
pip install pyyaml pyfiglet
```
