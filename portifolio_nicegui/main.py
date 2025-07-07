from nicegui import ui, app
from pathlib import Path

# Define the path to assets
ASSETS_PATH = Path(__file__).parent.parent / "assets"

# Custom CSS for styling
def setup_styles():
    ui.add_head_html("""
    <style>
        /* Import Google Fonts */
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');
        
        /* CSS Variables for consistent theming */
        :root {
            --primary-color: #6366f1;
            --primary-dark: #4f46e5;
            --secondary-color: #8b5cf6;
            --accent-color: #06b6d4;
            --text-primary: #1f2937;
            --text-secondary: #6b7280;
            --text-light: #9ca3af;
            --bg-primary: #ffffff;
            --bg-secondary: #f8fafc;
            --bg-accent: #f1f5f9;
            --border-color: #e2e8f0;
            --shadow-sm: 0 1px 2px 0 rgb(0 0 0 / 0.05);
            --shadow-md: 0 4px 6px -1px rgb(0 0 0 / 0.1), 0 2px 4px -2px rgb(0 0 0 / 0.1);
            --shadow-lg: 0 10px 15px -3px rgb(0 0 0 / 0.1), 0 4px 6px -4px rgb(0 0 0 / 0.1);
            --shadow-xl: 0 20px 25px -5px rgb(0 0 0 / 0.1), 0 8px 10px -6px rgb(0 0 0 / 0.1);
            --gradient-primary: linear-gradient(135deg, var(--primary-color) 0%, var(--secondary-color) 100%);
            --gradient-secondary: linear-gradient(135deg, var(--accent-color) 0%, var(--primary-color) 100%);
            --border-radius: 12px;
            --border-radius-lg: 16px;
            --transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
        }
        
        * {
            font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
        }
        
        .portfolio-container {
            width: 100%;
            margin: 0;
            padding: 0;
            background: var(--bg-secondary);
        }
        
        .content-wrapper {
            max-width: 1200px;
            margin: 0 auto;
            padding: 0 20px;
        }
        
        .section {
            margin-bottom: 80px;
            padding: 60px 0;
            transition: var(--transition);
        }
        
        .welcome-section {
            background: var(--gradient-primary);
            color: white;
            text-align: center;
            padding: 120px 20px;
            margin-bottom: 0;
            width: 100%;
            position: relative;
            overflow: hidden;
        }
        
        .welcome-section::before {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;
            background: url('data:image/svg+xml,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 100" fill="white" opacity="0.1"><path d="M0,50 Q250,0 500,50 T1000,50 L1000,100 L0,100 Z"/></svg>') repeat-x;
            background-size: 1000px 100px;
            background-position: bottom;
            animation: wave 20s linear infinite;
        }
        
        @keyframes wave {
            0% { background-position-x: 0; }
            100% { background-position-x: 1000px; }
        }
        
        .profile-pic {
            width: 200px;
            height: 200px;
            border-radius: 50%;
            object-fit: cover;
            border: 4px solid rgba(255, 255, 255, 0.9);
            box-shadow: var(--shadow-xl);
            transition: var(--transition);
            position: relative;
            z-index: 1;
        }
        
        .profile-pic:hover {
            transform: scale(1.05);
            box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.25);
        }
        
        .about-section {
            background: var(--bg-primary);
            color: var(--text-primary);
            border-radius: var(--border-radius-lg);
            padding: 50px;
            box-shadow: var(--shadow-lg);
            margin: 40px 0;
            font-size: 1.2em;
            line-height: 1.8;
            transition: var(--transition);
            border: 1px solid var(--border-color);
        }
        
        .about-section:hover {
            box-shadow: var(--shadow-xl);
            transform: translateY(-2px);
        }
        
        .about-section p {
            margin-bottom: 28px;
            text-align: justify;
            color: var(--text-secondary);
        }
        
        .about-section .highlight {
            background: var(--gradient-primary);
            background-clip: text;
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            font-weight: 600;
            font-size: 1.1em;
        }
        
        .about-section .emphasis {
            color: var(--primary-color);
            font-weight: 600;
        }
        
        .projects-section {
            background: var(--bg-primary);
            border-radius: var(--border-radius-lg);
            padding: 50px;
            margin: 40px 0;
            box-shadow: var(--shadow-lg);
            border: 1px solid var(--border-color);
            transition: var(--transition);
        }
        
        .projects-section:hover {
            box-shadow: var(--shadow-xl);
        }
        
        .resume-section {
            background: var(--bg-primary);
            border-radius: var(--border-radius-lg);
            padding: 50px;
            box-shadow: var(--shadow-lg);
            text-align: left;
            margin: 40px 0;
            font-size: 1.1em;
            line-height: 1.7;
            border: 1px solid var(--border-color);
            transition: var(--transition);
        }
        
        .resume-section:hover {
            box-shadow: var(--shadow-xl);
        }
        
        .resume-section h2 {
            text-align: center;
            margin-bottom: 50px;
            color: var(--text-primary);
        }
        
        .resume-section h3 {
            color: var(--primary-color);
            font-size: 1.6em;
            font-weight: 600;
            margin-top: 40px;
            margin-bottom: 25px;
            padding-bottom: 12px;
            border-bottom: 3px solid var(--primary-color);
            position: relative;
        }
        
        .resume-section h3::after {
            content: '';
            position: absolute;
            bottom: -3px;
            left: 0;
            width: 50px;
            height: 3px;
            background: var(--gradient-primary);
            border-radius: 2px;
        }
        
        .resume-section .contact-info {
            background: var(--gradient-primary);
            color: white;
            border-radius: var(--border-radius);
            padding: 30px;
            margin-bottom: 40px;
            text-align: center;
            box-shadow: var(--shadow-md);
            transition: var(--transition);
        }
        
        .resume-section .contact-info:hover {
            transform: translateY(-2px);
            box-shadow: var(--shadow-lg);
        }
        
        .resume-section .contact-info strong {
            font-size: 1.4em;
            color: white;
            font-weight: 600;
        }
        
        .resume-section .contact-info a {
            color: rgba(255, 255, 255, 0.9);
            text-decoration: none;
            transition: var(--transition);
        }
        
        .resume-section .contact-info a:hover {
            color: white;
            text-decoration: underline;
        }
        
        .resume-section .job-title {
            color: var(--primary-color);
            font-weight: 600;
            font-size: 1.2em;
        }
        
        .resume-section .company-name {
            color: var(--text-primary);
            font-weight: 600;
            font-size: 1.1em;
        }
        
        .resume-section .date-range {
            color: var(--text-light);
            font-style: italic;
            margin-left: 12px;
            font-weight: 500;
        }
        
        .resume-section .degree {
            color: var(--secondary-color);
            font-weight: 600;
            font-size: 1.1em;
        }
        
        .resume-section .institution {
            color: var(--text-primary);
            font-weight: 600;
        }
        
        .resume-section ul {
            margin: 20px 0;
            padding-left: 24px;
        }
        
        .resume-section li {
            margin-bottom: 12px;
            position: relative;
            color: var(--text-secondary);
            line-height: 1.6;
        }
        
        .resume-section li::marker {
            color: var(--primary-color);
        }
        
        .resume-section .highlight-achievement {
            background: linear-gradient(135deg, rgba(99, 102, 241, 0.1), rgba(139, 92, 246, 0.1));
            color: var(--primary-color);
            padding: 3px 8px;
            border-radius: 6px;
            font-weight: 600;
            border: 1px solid rgba(99, 102, 241, 0.2);
        }
        
        .resume-section .publication-item {
            background: var(--bg-accent);
            padding: 20px;
            margin: 15px 0;
            border-radius: var(--border-radius);
            border-left: 4px solid var(--primary-color);
            transition: var(--transition);
        }
        
        .resume-section .publication-item:hover {
            transform: translateX(5px);
            box-shadow: var(--shadow-md);
        }
        
        .resume-section .publication-journal {
            color: var(--primary-color);
            font-weight: 600;
        }
        
        .resume-section .publication-year {
            color: var(--text-light);
            font-weight: 600;
        }
        
        .section-title {
            font-size: 2.8em;
            font-weight: 700;
            margin-bottom: 40px;
            color: var(--text-primary);
            text-align: center;
            position: relative;
        }
        
        .section-title::after {
            content: '';
            position: absolute;
            bottom: -10px;
            left: 50%;
            transform: translateX(-50%);
            width: 80px;
            height: 4px;
            background: var(--gradient-primary);
            border-radius: 2px;
        }
        
        .welcome-title {
            font-size: 3.5em;
            font-weight: 700;
            margin-bottom: 25px;
            text-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
            position: relative;
            z-index: 1;
        }
        
        .welcome-subtitle {
            font-size: 1.6em;
            opacity: 0.95;
            margin-bottom: 40px;
            font-weight: 400;
            position: relative;
            z-index: 1;
        }
        
        .project-card {
            background: var(--bg-primary);
            padding: 40px;
            margin: 20px 0;
            border-radius: var(--border-radius-lg);
            transition: var(--transition);
            font-size: 1.1em;
            display: flex;
            flex-direction: column;
            justify-content: space-between;
            box-shadow: var(--shadow-md);
            border: 1px solid var(--border-color);
        }
        
        .project-card:hover {
            transform: translateY(-8px);
            box-shadow: var(--shadow-xl);
        }
        
        .project-card h3 {
            font-size: 1.8em;
            margin-bottom: 20px;
            color: var(--text-primary);
            font-weight: 600;
        }
        
        .project-card p {
            font-size: 1.1em;
            line-height: 1.7;
            margin-bottom: 16px;
            color: var(--text-secondary);
        }
        
        .project-header {
            display: flex;
            align-items: center;
            gap: 20px;
            margin-bottom: 25px;
        }
        
        .project-content {
            flex: 1;
        }
        
        .project-footer {
            margin-top: auto;
            padding-top: 25px;
            display: flex;
            justify-content: center;
            align-items: center;
            gap: 12px;
        }
        
        .details-btn, .github-btn {
            display: inline-flex;
            align-items: center;
            padding: 12px 24px;
            border-radius: var(--border-radius);
            font-size: 0.95em;
            font-weight: 500;
            text-decoration: none;
            transition: var(--transition);
            border: none;
            cursor: pointer;
            box-shadow: var(--shadow-sm);
        }
        
        .details-btn {
            background: var(--gradient-primary);
            color: white;
        }
        
        .details-btn:hover {
            transform: translateY(-2px);
            box-shadow: var(--shadow-md);
        }
        
        .github-btn {
            background: var(--text-primary);
            color: white;
        }
        
        .github-btn:hover {
            background: var(--text-secondary);
            transform: translateY(-2px);
            box-shadow: var(--shadow-md);
        }
        
        .modal-text-content {
            color: var(--text-secondary);
            line-height: 1.7;
        }
        
        .modal-text-content h4 {
            color: var(--primary-color);
            font-size: 1.6em;
            margin-bottom: 25px;
            text-align: center;
            font-weight: 600;
        }
        
        .modal-text-content .story-section {
            margin-bottom: 25px;
        }
        
        .modal-text-content .story-section h5 {
            color: var(--secondary-color);
            font-size: 1.3em;
            margin-bottom: 15px;
            font-weight: 600;
        }
        
        .modal-text-content ul {
            margin-left: 24px;
            margin-bottom: 20px;
        }
        
        .modal-text-content li {
            margin-bottom: 10px;
            line-height: 1.6;
        }
        
        .modal-text-content .tech-stack {
            background: var(--bg-accent);
            padding: 20px;
            border-radius: var(--border-radius);
            margin-bottom: 20px;
            border: 1px solid var(--border-color);
        }
        
        .modal-text-content .tech-stack strong {
            color: var(--primary-color);
        }
        
        .modal-text-content p {
            line-height: 1.7;
            margin-bottom: 18px;
        }
        
        /* Navigation Styles */
        .nav-container {
            position: fixed;
            top: 0;
            left: 0;
            right: 0;
            z-index: 1000;
            background: rgba(255, 255, 255, 0.95);
            backdrop-filter: blur(20px);
            border-bottom: 1px solid var(--border-color);
            transition: var(--transition);
        }
        
        .nav-container button {
            color: var(--text-secondary);
            font-weight: 500;
            padding: 8px 16px;
            margin: 0 4px;
            border-radius: var(--border-radius);
            transition: var(--transition);
            background: transparent;
            border: none;
        }
        
        .nav-container button:hover {
            background: var(--primary-color);
            color: #fff;
            transform: translateY(-1px);
        }
        
        /* Back to top button */
        .back-to-top {
            position: fixed;
            bottom: 30px;
            right: 30px;
            z-index: 1000;
            background: var(--gradient-primary);
            color: white;
            border: none;
            border-radius: 50%;
            width: 56px;
            height: 56px;
            font-size: 1.5em;
            cursor: pointer;
            box-shadow: var(--shadow-lg);
            transition: var(--transition);
        }
        
        .back-to-top:hover {
            transform: translateY(-3px);
            box-shadow: var(--shadow-xl);
        }
        
        /* Responsive Design */
        @media (max-width: 768px) {
            .content-wrapper {
                padding: 0 16px;
            }
            
            .welcome-title {
                font-size: 2.5em;
            }
            
            .section-title {
                font-size: 2.2em;
            }
            
            .about-section, .projects-section, .resume-section {
                padding: 30px;
            }
            
            .project-card {
                padding: 30px;
            }
        }
        
        /* Smooth scroll behavior */
        html {
            scroll-behavior: smooth;
        }
    </style>
    """)

def create_welcome_about_section():
    """Create the combined welcome and about section"""
    with ui.element('div').classes('welcome-section'):
        with ui.element('div').classes('content-wrapper'):
            ui.html('<h1 class="welcome-title">Hello, I\'m <strong>Marcus</strong></h1>')
            ui.html('<p class="welcome-subtitle">Hiker. Researcher. Developer.</p>')
            
            # Check if profile image exists
            profile_path = ASSETS_PATH / "images" / "profile.jpeg"
            if profile_path.exists():
                ui.image('/assets/images/profile.jpeg').classes('profile-pic')
            else:
                ui.label('👨‍💻').style('font-size: 100px; margin: 20px 0;')
            
            # About Me content integrated into welcome section
            with ui.element('div').classes('about-section').style('background: rgba(255,255,255,0.95); margin-top: 40px;'):
                ui.html('<h2 class="section-title" style="color: #333;">About Me</h2>')
                
                ui.html("""
                <p>My journey into <span class="highlight">problem-solving and automation</span> began in 2014, during my time in scientific research. 
                It was there that I discovered the power of using <span class="emphasis">programming to streamline tasks</span> and uncover insights.</p>
                
                <p>Since then, I've been deeply passionate about using <span class="highlight">technology to improve efficiency</span> and solve complex challenges. 
                What started as a curiosity has evolved into a versatile skill set that spans <span class="emphasis">automation, data analysis, and intuitive software development</span>.</p>
                
                <p>I've had the opportunity to work on diverse projects — from building <span class="emphasis">automation pipelines for scientific workflows</span> 
                to crafting <span class="emphasis">user-friendly interfaces for data interaction</span>. Each experience has strengthened both my technical and problem-solving capabilities.</p>
                
                <p>I'm a firm believer in <span class="highlight">continuous learning</span> and always strive to stay current with modern tools, languages, and development practices.</p>
                
                <p><strong style="font-size: 1.2em; color: #667eea;">Let's collaborate to turn challenging problems into elegant, impactful solutions.</strong></p>
                """)

def create_projects_section():
    """Create the projects section"""
    with ui.element('div').classes('content-wrapper'):
        with ui.element('div').classes('projects-section'):
            ui.html('<h2 class="section-title">My Selected (Open) Projects</h2>')
            
            projects = [
                {
                    'title': 'TrackIT',
                    'description': 'Complete application for tracking objects in video using OpenCV with full-stack implementation.',
                    'tech': 'Python, FastAPI, SQLAlchemy, Angular, PostgreSQL',
                    'github': 'https://github.com/mv-per/TrackIt',
                    'icon': '🎥',
                    'detailed_description': '''
                        <h4>TrackIT - Object Tracking Application</h4>
                        <p><strong>Client Need:</strong> A comprehensive application to track objects in video with user management and simulation capabilities.</p>
                        
                        <div class="story-section">
                            <h5>Key Features:</h5>
                            <ul>
                                <li>Track objects in video using OpenCV</li>
                                <li>Complete user management system with SQL database</li>
                                <li>Backend API for video loading, simulation execution, and download</li>
                                <li>Frontend application with login, video management, and simulation controls</li>
                                <li>Customizable simulation options (line length, color, tracking algorithms)</li>
                                <li>Real-time progress tracking and video download functionality</li>
                            </ul>
                        </div>
                        
                        <div class="tech-stack">
                            <strong>Backend:</strong> Python + FastAPI + SQLAlchemy + Alembic<br>
                            <strong>Frontend:</strong> Angular2 + PrimeNG<br>
                            <strong>Database:</strong> PostgreSQL (SQLAlchemy compatible)
                        </div>
                        
                        <p><em>Full-stack solution delivering complete object tracking capabilities with professional user interface.</em></p>
                    '''
                },
                {
                    'title': 'CheML',
                    'description': 'Comprehensive Python toolkit for machine learning in Chemical Engineering with production-ready features.',
                    'tech': 'Python, scikit-learn, FastAPI, MLflow, Conda',
                    'github': 'https://github.com/mv-per/cheml',
                    'icon': '🧪',
                    'detailed_description': '''
                        <h4>CheML - Chemical Engineering ML Toolkit</h4>
                        <p><strong>Comprehensive Python toolkit for machine learning in Chemical Engineering</strong></p>
                        
                        <div class="story-section">
                            <h5>Core Features:</h5>
                            <ul>
                                <li><strong>ML Model Templates:</strong> Pre-built scikit-learn workflows</li>
                                <li><strong>Manufacturing Quality Prediction:</strong> FastAPI-based prediction endpoints</li>
                                <li><strong>MLflow Integration:</strong> Complete experiment tracking and model management</li>
                                <li><strong>Process Optimization:</strong> Advanced algorithms for chemical processes</li>
                                <li><strong>Real-time Predictions:</strong> Production endpoints with input validation</li>
                            </ul>
                        </div>
                        
                        <div class="story-section">
                            <h5>Applications:</h5>
                            <ul>
                                <li>Reaction yield forecasting</li>
                                <li>Quality control systems</li>
                                <li>Process optimization</li>
                                <li>Chemical property estimation</li>
                            </ul>
                        </div>
                        
                        <div class="tech-stack">
                            <strong>Production Features:</strong> Conda environments, pre-commit hooks, comprehensive documentation, scalable architecture for industrial chemical engineering applications.
                        </div>
                    '''
                }
            ]
            
            for project in projects:
                with ui.element('div').classes('project-card'):
                    # Project header with icon
                    with ui.element('div').classes('project-header'):
                        ui.html(f'<div style="font-size: 3em; margin-right: 15px;">{project["icon"]}</div>')
                        ui.html(f'<h3 style="margin: 0;">{project["title"]}</h3>')
                    
                    # Project content
                    with ui.element('div').classes('project-content'):
                        ui.html(f'<p>{project["description"]}</p>')
                        ui.html(f'<p><strong>Technologies:</strong> {project["tech"]}</p>')
                    
                    # Project footer with buttons
                    with ui.element('div').classes('project-footer'):
                        # Details button that opens modal
                        def create_details_handler(project_data):
                            def show_details():
                                with ui.dialog() as dialog:
                                    with ui.card().style('max-width: 800px; max-height: 80vh; overflow-y: auto;'):
                                        with ui.element('div').classes('modal-text-content'):
                                            ui.html(project_data['detailed_description'])
                                        with ui.card_actions().classes('justify-end'):
                                            ui.button('Close', on_click=dialog.close)
                                    dialog.open()
                            return show_details
                        
                        with ui.row().classes('gap-2'):
                            ui.button('Details', on_click=create_details_handler(project)).classes('details-btn')
                            ui.link('View on GitHub', project['github'], new_tab=True).classes('github-btn')

def create_resume_section():
    """Create the resume section with extracted HTML content instead of a downloadable PDF"""
    with ui.element('div').classes('content-wrapper'):
        with ui.element('div').classes('resume-section'):
            ui.html('<h2 class="section-title">My Resume</h2>')

            # Professional Summary
            ui.html('<h3>🎯 Professional Summary</h3>')
            ui.html('''
                <p style="font-size: 1.1em; color: #555; margin-bottom: 25px;">
                    <strong>Chemical Engineer</strong> with expertise in <span class="highlight-achievement">software development</span>, 
                    <span class="highlight-achievement">data analysis</span>, and <span class="highlight-achievement">automation</span>. 
                    Passionate about applying technology to solve complex engineering challenges and optimize industrial processes.
                </p>
            ''')

            # Work Experience
            ui.html('<h3>💼 Work Experience</h3>')
            ui.html('''
                <div style="margin-bottom: 25px;">
                    <p><span class="company-name">Engineering Simulation and Scientific Software</span> 
                    <span class="date-range">(2021–2024)</span><br>
                    <span class="job-title">Software Developer</span></p>
                    <ul>
                        <li>Optimized SQL queries and caching strategies achieving a <span class="highlight-achievement">30% improvement</span> in backend response time</li>
                        <li>Developed <span class="highlight-achievement">Angular components</span> for enhanced data management and user experience</li>
                        <li>Built <span class="highlight-achievement">microservices infrastructure</span> to accelerate simulation workflows and boost scalability</li>
                        <li>Implemented <span class="highlight-achievement">GitHub Actions CI/CD</span> for automated code validation and formatting</li>
                        <li>Streamlined deployment processes, reducing release time by <span class="highlight-achievement">20%</span></li>
                    </ul>
                </div>
                
                <div style="margin-bottom: 25px;">
                    <p><span class="company-name">Laboratory of Adsorption and Ion Exchange</span> 
                    <span class="date-range">(2018–2021)</span><br>
                    <span class="job-title">Junior Researcher</span> | <em>Brazil</em></p>
                    <ul>
                        <li>Led training programs for <span class="highlight-achievement">15+ students and interns</span> on lab and field research methodologies</li>
                        <li>Designed and operated <span class="highlight-achievement">high-pressure adsorption systems</span> for gas separation research</li>
                        <li>Automated data acquisition systems improving research workflow <span class="highlight-achievement">efficiency by 40%</span></li>
                        <li>Developed <span class="highlight-achievement">multicomponent adsorption algorithms</span> in Python and C/C++</li>
                    </ul>
                </div>
            ''')

            # Education
            ui.html('<h3>🎓 Education</h3>')
            ui.html('''
                <div style="margin-bottom: 20px;">
                    <p><span class="degree">Ph.D. in Chemical Engineering</span><br>
                    <span class="institution">Louisiana State University, USA</span> <span class="date-range">(2024–Present)</span><br>
                    <em>Focus: Machine Learning for Sustainable Chemical Manufacturing</em></p>
                </div>
                
                <div style="margin-bottom: 20px;">
                    <p><span class="degree">M.Sc. in Chemical Engineering</span><br>
                    <span class="institution">State University of Maringá, Brazil</span> <span class="date-range">(2016–2019)</span><br>
                    <em>Focus: Adsorption modeling using Potential Theory</em></p>
                </div>
                
                <div style="margin-bottom: 20px;">
                    <p><span class="degree">B.Tech. in Chemical Processes</span><br>
                    <span class="institution">Federal University of Technology, Brazil</span> <span class="date-range">(2011–2016)</span></p>
                </div>
                
                <div style="margin-bottom: 20px;">
                    <p><span class="degree">Academic Exchange Program</span><br>
                    <span class="institution">University of Nevada, Reno, USA</span> <span class="date-range">(2014–2015)</span></p>
                </div>
            ''')

            # Technical Skills
            ui.html('<h3>🔧 Technical Skills</h3>')
            ui.html('''
                <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 20px; margin-bottom: 25px;">
                    <div>
                        <p><strong style="color: #667eea;">Programming Languages:</strong><br>
                        Python, TypeScript, JavaScript, C/C++, MATLAB</p>
                    </div>
                    <div>
                        <p><strong style="color: #667eea;">Web Technologies:</strong><br>
                        Angular, HTML/CSS, NiceGUI, REST APIs</p>
                    </div>
                    <div>
                        <p><strong style="color: #667eea;">Data & Analytics:</strong><br>
                        SQL, Data Analysis, Machine Learning, Automation</p>
                    </div>
                    <div>
                        <p><strong style="color: #667eea;">Tools & Platforms:</strong><br>
                        Git, GitHub Actions, Docker, Microservices, MLFlow</p>
                    </div>
                </div>
            ''')

            # Research Experience
            ui.html('<h3>🔬 Research Experience</h3>')
            ui.html('''
                <div style="margin-bottom: 20px;">
                    <p><span class="institution">State University of Maringá, Brazil</span><br>
                    <em>Multicomponent adsorption modeling using Potential Theory on zeolites and activated carbon for gas separation applications</em></p>
                </div>
                
                <div style="margin-bottom: 20px;">
                    <p><span class="institution">University of Nevada, Reno, USA</span><br>
                    <em>Hydrodeoxygenation of biocrude and catalytic biomass conversion for sustainable biofuel production</em></p>
                </div>
            ''')

            # Publications
            ui.html('<h3>📚 Selected Publications</h3>')
            ui.html('''
                <div class="publication-item">
                    <span class="publication-journal">Separation and Purification Technology</span> 
                    <span class="publication-year">(2025)</span><br>
                    <em>"CO₂ adsorption in NaY zeolite beds: Modeling and optimization"</em>
                </div>
                
                <div class="publication-item">
                    <span class="publication-journal">Adsorption</span> 
                    <span class="publication-year">(2023)</span><br>
                    <em>"Simulation of sour gas adsorption using multicomponent theory"</em>
                </div>
                
                <div class="publication-item">
                    <span class="publication-journal">Journal of CO₂ Utilization</span> 
                    <span class="publication-year">(2023)</span><br>
                    <em>"Zeolite regeneration for cyclic CO₂ capture applications"</em>
                </div>
                
                <div class="publication-item">
                    <span class="publication-journal">Chemical Engineering Science</span> 
                    <span class="publication-year">(2022)</span><br>
                    <em>"Confined fluid isotherms with PCP-SAFT DFT modeling"</em>
                </div>
                
                <div class="publication-item">
                    <span class="publication-journal">Microporous and Mesoporous Materials</span> 
                    <span class="publication-year">(2019)</span><br>
                    <em>"H₂S adsorption on NaY zeolite: Experimental and theoretical analysis"</em>
                </div>
            ''')

            ui.html('<br>')

def create_contact_section():
    """Create the contact section"""
    with ui.element('div').classes('content-wrapper'):
        with ui.element('div').classes('contact-section resume-section'):
            ui.html('<h2 class="section-title">Contact Information</h2>')

            
            # Contact buttons
            with ui.row().classes('justify-center gap-4').style('margin-top: 30px;'):
                ui.link('📧 Email', 'mailto:mav.pereira@outlook.com', new_tab=True).classes('details-btn').style('background: var(--gradient-primary); color: white; text-decoration: none;')
                ui.link('💼 LinkedIn', 'https://linkedin.com/in/marcusvpereira', new_tab=True).classes('github-btn').style('background: #0077b5; color: white; text-decoration: none;')
                ui.link('🎓 ORCID', 'https://orcid.org/0000-0003-2405-5308', new_tab=True).classes('github-btn').style('background: #a6ce39; color: white; text-decoration: none;')
            

def create_navigation():
    """Create a simple navigation bar"""
    with ui.row().classes('w-full justify-center nav-container').style('padding: 20px;'):
        ui.button('Welcome', on_click=lambda: ui.run_javascript('document.querySelector(".welcome-section").scrollIntoView({behavior: "smooth"});')).props('flat')
        ui.button('About', on_click=lambda: ui.run_javascript('document.querySelector(".about-section").scrollIntoView({behavior: "smooth"});')).props('flat')
        ui.button('Projects', on_click=lambda: ui.run_javascript('document.querySelector(".projects-section").scrollIntoView({behavior: "smooth"});')).props('flat')
        ui.button('Resume', on_click=lambda: ui.run_javascript('document.querySelector(".resume-section").scrollIntoView({behavior: "smooth"});')).props('flat')
        ui.button('Contact', on_click=lambda: ui.run_javascript('document.querySelector(".contact-section").scrollIntoView({behavior: "smooth"});')).props('flat')

def setup_static_files():
    """Set up static file serving for assets"""
    assets_dir = ASSETS_PATH
    if assets_dir.exists():
        app.add_static_files('/assets', str(assets_dir))

def main():
    """Main function to create the portfolio"""
    setup_styles()
    setup_static_files()
    
    # Set page title and meta
    ui.page_title('Marcus - Portfolio')
    ui.add_head_html('<meta name="viewport" content="width=device-width, initial-scale=1.0">')
    
    # Add smooth scrolling to body
    ui.add_head_html('<script>document.documentElement.style.scrollBehavior = "smooth";</script>')
    
    # Create navigation
    create_navigation()
    
    # Main container with top padding for fixed nav
    with ui.element('div').classes('portfolio-container').style('padding-top: 0;'):
        create_welcome_about_section()
        create_projects_section()
        create_resume_section()
        create_contact_section()
    
    # Add a "Back to Top" button
    ui.button('↑', on_click=lambda: ui.run_javascript('window.scrollTo({top: 0, behavior: "smooth"});')).props('fab').classes('back-to-top')

async def save():
    # Only save if there's a specific client context
    try:
        from nicegui import context
        if hasattr(context, 'client') and context.client:
            html = await context.client.run_javascript("document.querySelector('html').outerHTML")
            with open("./index.html", "w", encoding="utf-8") as file:
                file.write(html)
            print("Portfolio saved successfully!")
        else:
            create_basic_html_structure()
    except Exception as e:
        print(f"Could not save HTML from client: {e}")
        create_basic_html_structure()

def create_basic_html_structure():
    """Create a basic HTML structure when client context is not available"""
    basic_html = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Marcus - Portfolio</title>
    <style>
        /* Add your CSS styles here */
        body { font-family: Arial, sans-serif; margin: 0; padding: 20px; }
        .container { max-width: 1200px; margin: 0 auto; }
        h1 { color: #333; text-align: center; }
    </style>
</head>
<body>
    <div class="container">
        <h1>Marcus - Portfolio</h1>
        <p>This is a basic HTML structure. Please visit the live site for the full experience.</p>
        <p>Live site: <a href="http://localhost:8081">http://localhost:8081</a></p>
    </div>
</body>
</html>"""
    
    with open("./index.html", "w", encoding="utf-8") as file:
        file.write(basic_html)
    print("Created basic HTML structure...")

# Alternative approach: Use a button-triggered save instead of timer
def save_on_demand():
    async def do_save():
        try:
            from nicegui import context
            if hasattr(context, 'client') and context.client:
                # Get the complete HTML including all rendered content and styles
                html = await context.client.run_javascript("""
                    // Get the complete document HTML with all styles and scripts
                    const fullHtml = document.documentElement.outerHTML;
                    
                    // Clean up NiceGUI-specific elements that won't work standalone
                    const parser = new DOMParser();
                    const doc = parser.parseFromString(fullHtml, 'text/html');
                    
                    // Remove NiceGUI-specific scripts and components
                    const scriptsToRemove = doc.querySelectorAll('script[src*="_nicegui"]');
                    scriptsToRemove.forEach(script => script.remove());
                    
                    // Remove NiceGUI app components
                    const appDiv = doc.querySelector('#app');
                    if (appDiv) {
                        // Extract the actual content from the app div
                        const content = appDiv.innerHTML;
                        appDiv.innerHTML = content;
                    }
                    
                    // Add standalone JavaScript for navigation
                    const standaloneScript = document.createElement('script');
                    standaloneScript.textContent = `
                        document.addEventListener('DOMContentLoaded', function() {
                            // Smooth scroll functionality
                            function smoothScrollTo(selector) {
                                const element = document.querySelector(selector);
                                if (element) {
                                    element.scrollIntoView({behavior: 'smooth'});
                                }
                            }
                            
                            // Back to top functionality
                            function scrollToTop() {
                                window.scrollTo({top: 0, behavior: 'smooth'});
                            }
                            
                            // Re-attach event listeners for navigation buttons
                            document.querySelectorAll('button').forEach(btn => {
                                const text = btn.textContent.trim();
                                if (text === 'Welcome') {
                                    btn.onclick = () => smoothScrollTo('.welcome-section');
                                } else if (text === 'About') {
                                    btn.onclick = () => smoothScrollTo('.about-section');
                                } else if (text === 'Projects') {
                                    btn.onclick = () => smoothScrollTo('.projects-section');
                                } else if (text === 'Resume') {
                                    btn.onclick = () => smoothScrollTo('.resume-section');
                                } else if (text === 'Contact') {
                                    btn.onclick = () => smoothScrollTo('.contact-section');
                                } else if (text === '↑') {
                                    btn.onclick = scrollToTop;
                                } else if (text === 'Details') {
                                    // Keep existing modal functionality
                                    // This will need to be handled separately
                                }
                            });
                            
                            // Show/hide back to top button
                            window.addEventListener('scroll', function() {
                                const backToTopBtn = document.querySelector('.back-to-top');
                                if (backToTopBtn) {
                                    if (window.pageYOffset > 300) {
                                        backToTopBtn.style.opacity = '1';
                                        backToTopBtn.style.visibility = 'visible';
                                    } else {
                                        backToTopBtn.style.opacity = '0';
                                        backToTopBtn.style.visibility = 'hidden';
                                    }
                                }
                            });
                            
                            // Handle GitHub links
                            document.querySelectorAll('a[href*="github.com"]').forEach(link => {
                                link.target = '_blank';
                                link.rel = 'noopener noreferrer';
                            });
                            
                            // Handle email and other external links
                            document.querySelectorAll('a[href^="mailto:"], a[href^="https://linkedin.com"], a[href^="https://orcid.org"]').forEach(link => {
                                link.target = '_blank';
                                link.rel = 'noopener noreferrer';
                            });
                        });
                    `;
                    
                    // Remove the save button from the exported HTML
                    const saveButton = doc.querySelector('button[style*="position: fixed"][style*="top: 10px"]');
                    if (saveButton) {
                        saveButton.remove();
                    }
                    
                    // Remove any NiceGUI notification elements
                    const notifications = doc.querySelectorAll('[id*="q-notify"], [data-v-app]');
                    notifications.forEach(el => el.remove());
                    
                    // Add the standalone script to the body
                    doc.body.appendChild(standaloneScript);
                    
                    // Add smooth scrolling CSS if not present
                    if (!doc.querySelector('style[data-smooth-scroll]')) {
                        const smoothScrollStyle = document.createElement('style');
                        smoothScrollStyle.setAttribute('data-smooth-scroll', 'true');
                        smoothScrollStyle.textContent = `
                            html { scroll-behavior: smooth; }
                            .back-to-top { opacity: 0; visibility: hidden; transition: all 0.3s ease; }
                            .back-to-top.show { opacity: 1; visibility: visible; }
                        `;
                        doc.head.appendChild(smoothScrollStyle);
                    }
                    
                    return '<!DOCTYPE html>\\n' + doc.documentElement.outerHTML;
                """)
                
                # Write the cleaned HTML to file
                with open("./index.html", "w", encoding="utf-8") as file:
                    file.write(html)
                    
                ui.notify("Portfolio extracted and saved as standalone index.html!", type='positive')
                print("Portfolio successfully extracted from live website!")
                
            else:
                create_basic_html_structure()
                ui.notify("No client context available, created basic structure", type='warning')
                
        except Exception as e:
            print(f"Error extracting from website: {e}")
            create_basic_html_structure()
            ui.notify(f"Error extracting: {e}", type='negative')
    return do_save

if __name__ in {"__main__", "__mp_main__"}:
    # Create a specific page instead of using auto-index
    @ui.page('/')
    def index():
        main()
        # Add save button for manual saving
        ui.button("Save Portfolio", on_click=save_on_demand()).style('position: fixed; top: 10px; right: 10px; z-index: 1000;')
    
    ui.run(title='Marcus - Portfolio', port=8081, show=True)

