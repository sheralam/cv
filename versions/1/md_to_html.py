#!/usr/bin/env python3
"""
Convert Markdown CV to HTML using the existing template design.
This script parses khaja.md and generates an HTML file with the same styling.
"""

import re
import sys
from pathlib import Path


def parse_markdown_cv(md_content):
    """Parse the markdown CV into structured sections."""
    lines = md_content.strip().split('\n')
    
    data = {
        'name': '',
        'subtitle': '',
        'contact': '',
        'linkedin': '',
        'impact_summary': [],
        'technical_expertise': [],
        'experiences': [],
        'education': []
    }
    
    current_section = None
    current_experience = None
    i = 0
    
    while i < len(lines):
        line = lines[i].strip()
        
        # Parse name (## heading)
        if line.startswith('## ') and not data['name']:
            data['name'] = line[3:].strip()
            i += 1
            # Next line should be the subtitle
            if i < len(lines):
                subtitle_line = lines[i].strip()
                # Extract subtitle text before location
                match = re.match(r'\*\*(.*?)\*\*\s*(.*)', subtitle_line)
                if match:
                    data['subtitle'] = match.group(1).strip()
                    rest = match.group(2).strip()
                    # Extract email
                    email_match = re.search(r'\[([^\]]+@[^\]]+)\]', rest)
                    if email_match:
                        data['contact'] = email_match.group(1)
                    # Extract LinkedIn
                    linkedin_match = re.search(r'\[LinkedIn\]\(([^\)]+)\)', rest)
                    if linkedin_match:
                        data['linkedin'] = linkedin_match.group(1)
        
        # Parse sections
        elif line.startswith('### '):
            section_title = line[4:].strip()
            current_section = section_title.lower()
            
            if 'impact' in current_section:
                current_section = 'impact'
            elif 'expertise' in current_section or 'technical' in current_section:
                current_section = 'expertise'
            elif 'experience' in current_section:
                current_section = 'experience'
            elif 'education' in current_section:
                current_section = 'education'
        
        # Parse list items
        elif line.startswith('* ') or line.startswith('- '):
            item = line[2:].strip()
            
            if current_section == 'impact':
                data['impact_summary'].append(item)
            elif current_section == 'expertise':
                data['technical_expertise'].append(item)
            elif current_section == 'education':
                data['education'].append(item)
            elif current_section == 'experience' and current_experience:
                current_experience['achievements'].append(item)
        
        # Parse experience entries (#### heading)
        elif line.startswith('#### '):
            if current_section == 'experience':
                # Parse company and title
                company_line = line[5:].strip()
                match = re.match(r'\*\*([^\*]+)\*\*\s*\|\s*(.+)', company_line)
                if match:
                    current_experience = {
                        'company': match.group(1).strip(),
                        'title': match.group(2).strip(),
                        'location': '',
                        'period': '',
                        'achievements': []
                    }
                    data['experiences'].append(current_experience)
        
        # Parse experience metadata (italic line)
        elif line.startswith('*') and not line.startswith('**') and current_experience:
            # Parse location and dates
            meta_line = line.strip('*').strip()
            match = re.match(r'([^|]+)\|\s*(.+)', meta_line)
            if match:
                current_experience['location'] = match.group(1).strip()
                current_experience['period'] = match.group(2).strip()
        
        i += 1
    
    return data


def clean_markdown(text):
    """Remove markdown formatting from text."""
    # Remove bold markers
    text = re.sub(r'\*\*([^\*]+)\*\*', r'\1', text)
    # Remove italic markers
    text = re.sub(r'\*([^\*]+)\*', r'\1', text)
    return text


def generate_html(data, template_path=None):
    """Generate HTML from parsed data using the template style."""
    
    # Generate impact summary HTML
    impact_html = []
    for item in data['impact_summary']:
        item = clean_markdown(item)
        # Bold the first part before colon
        if ':' in item:
            parts = item.split(':', 1)
            impact_html.append(f'<li><strong>{parts[0]}:</strong>{parts[1]}</li>')
        else:
            impact_html.append(f'<li>{item}</li>')
    
    impact_section = '\n                '.join(impact_html)
    
    # Generate technical expertise HTML
    expertise_html = []
    for item in data['technical_expertise']:
        item = clean_markdown(item)
        # Bold the first part before colon
        if ':' in item:
            parts = item.split(':', 1)
            expertise_html.append(f'<div class="skill-group"><b>{parts[0]}:</b>{parts[1]}</div>')
        else:
            expertise_html.append(f'<div class="skill-group">{item}</div>')
    
    expertise_section = '\n            '.join(expertise_html)
    
    # Generate experience HTML
    experience_blocks = []
    for exp in data['experiences']:
        achievements = []
        for achievement in exp['achievements']:
            achievement = clean_markdown(achievement)
            # Bold the first part before colon
            if ':' in achievement:
                parts = achievement.split(':', 1)
                achievements.append(f'<li><strong>{parts[0]}:</strong>{parts[1]}</li>')
            else:
                achievements.append(f'<li>{achievement}</li>')
        
        achievements_html = '\n                '.join(achievements)
        
        exp_block = f'''
        <div class="experience-block">
            <div class="job-header"><span>{exp['company']}</span> <span>{exp['period']}</span></div>
            <div class="job-sub"><span>{exp['title']}</span> <span>{exp['location']}</span></div>
            <ul>
                {achievements_html}
            </ul>
        </div>'''
        experience_blocks.append(exp_block)
    
    experience_section = '\n'.join(experience_blocks)
    
    # Generate education HTML
    education_html = []
    for edu in data['education']:
        edu = clean_markdown(edu)
        education_html.append(f'<div class="job-header"><span>{edu}</span></div>')
    
    education_section = '\n        '.join(education_html)
    
    # Extract location from contact info
    location = "Berlin, Germany"
    
    # Generate the full HTML
    html = f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Khaja_Md_Sher_E_Alam_Staff_Engineer_CV</title>
    <style>
        body {{ font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; line-height: 1.5; color: #1a1a1a; margin: 0; padding: 40px; background-color: #fff; }}
        .container {{ max-width: 900px; margin: auto; }}
        header {{ border-bottom: 3px solid #2c3e50; padding-bottom: 15px; margin-bottom: 25px; }}
        h1 {{ margin: 0; font-size: 28px; color: #2c3e50; text-transform: uppercase; letter-spacing: 1px; }}
        .contact-info {{ margin-top: 8px; font-size: 14px; color: #444; }}
        .contact-info a {{ color: #2980b9; text-decoration: none; font-weight: bold; }}
        
        h2 {{ font-size: 18px; border-bottom: 1px solid #bdc3c7; color: #2c3e50; text-transform: uppercase; margin-top: 30px; margin-bottom: 12px; letter-spacing: 1px; }}
        
        .highlight-box {{ background-color: #f8f9fa; border-left: 5px solid #2c3e50; padding: 15px; margin-bottom: 20px; }}
        .highlight-box ul {{ margin: 0; padding-left: 20px; list-style-type: square; }}
        .highlight-box li {{ margin-bottom: 5px; font-size: 14px; }}

        .job-header {{ display: flex; justify-content: space-between; align-items: baseline; font-weight: bold; font-size: 16px; margin-top: 20px; color: #2c3e50; }}
        .job-sub {{ display: flex; justify-content: space-between; font-style: italic; font-size: 14px; color: #7f8c8d; margin-bottom: 10px; }}
        
        ul {{ margin-top: 5px; padding-left: 20px; }}
        li {{ margin-bottom: 8px; font-size: 14px; text-align: justify; }}
        
        .skills-container {{ display: flex; flex-wrap: wrap; gap: 10px; font-size: 13px; }}
        .skill-group {{ flex: 1 1 45%; margin-bottom: 10px; }}
        .skill-group b {{ color: #2c3e50; display: block; margin-bottom: 2px; }}

        @media print {{
            body {{ padding: 0; }}
            .container {{ width: 100%; }}
            header {{ border-bottom-width: 2px; }}
        }}
    </style>
</head>
<body>

<div class="container">
    <header>
        <h1>{data['name']}</h1>
        <div class="contact-info">
            <strong>{data['subtitle']}</strong><br>
            {location} | <a href="mailto:{data['contact']}">{data['contact']}</a> | 
            <a href="{data['linkedin']}">{data['linkedin'].replace('https://', '')}</a>
        </div>
    </header>

    <section>
        <h2>Staff-Level Impact Summary</h2>
        <div class="highlight-box">
            <ul>
                {impact_section}
            </ul>
        </div>
    </section>

    <section>
        <h2>Core Technical Expertise</h2>
        <div class="skills-container">
            {expertise_section}
        </div>
    </section>

    <section>
        <h2>Professional Experience</h2>
{experience_section}
    </section>

    <section>
        <h2>Education</h2>
        {education_section}
    </section>
</div>

</body>
</html>'''
    
    return html


def main():
    """Main function to convert markdown to HTML."""
    if len(sys.argv) < 2:
        print("Usage: python md_to_html.py <input.md> [output.html]")
        print("Example: python md_to_html.py khaja.md khaja.html")
        sys.exit(1)
    
    input_file = Path(sys.argv[1])
    
    if not input_file.exists():
        print(f"Error: Input file '{input_file}' not found.")
        sys.exit(1)
    
    # Determine output filename
    if len(sys.argv) >= 3:
        output_file = Path(sys.argv[2])
    else:
        output_file = input_file.with_suffix('.html')
    
    # Read markdown content
    print(f"Reading {input_file}...")
    with open(input_file, 'r', encoding='utf-8') as f:
        md_content = f.read()
    
    # Parse and convert
    print("Parsing markdown content...")
    data = parse_markdown_cv(md_content)
    
    print("Generating HTML...")
    html = generate_html(data)
    
    # Write output
    print(f"Writing to {output_file}...")
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(html)
    
    print(f"✓ Successfully converted {input_file} to {output_file}")


if __name__ == '__main__':
    main()
