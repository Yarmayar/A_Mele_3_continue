from weasyprint import HTML
HTML('https://weasyprint.org/').write_pdf('/tmp/weasyprint-website.pdf')