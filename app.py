from flask import Flask, render_template
import datetime

app = Flask(__name__)

@app.route('/')
def home():
    experience = [
        {
            'title': 'Head of Department (Software)',
            'company': 'AYA Bank',
            'period': '2020 - Present',
            'key_achievements': [
                'Successfully implemented and maintained PCI-DSS 3.2.2 and 3.2.3 compliance across all payment systems',
                'Led end-to-end implementation of new AYAPay version, resulting in improved user experience and increased transaction volume',
                'Managed multiple critical banking infrastructure projects with 100% success rate',
                'Established robust payment processing systems handling millions of transactions monthly',
                'Successfully integrated multiple international payment schemes (Visa, Mastercard, JCB, UPI)',
                'Achieved significant improvement in system reliability and transaction processing efficiency',
                'Led digital transformation initiatives resulting in enhanced customer experience'
            ],
            'responsibilities': [
                {
                    'category': 'Digital Banking Leadership',
                    'description': [
                        'Managing end-to-end implementation of new AYAPay version, including:',
                        '- Modern UI/UX design and implementation',
                        '- Native mobile application development for iOS and Android',
                        '- Integration with core banking systems',
                        '- Business requirement analysis and implementation',
                        'Leading AYA Innolabs team across multiple products:',
                        '- AYAPAY mobile wallet and payment solutions',
                        '- Partner integration applications and APIs',
                        '- Agency Banking platform development',
                        '- Teller and Customer service applications',
                        '- Mobile Banking platform enhancement',
                        'Overseeing new Mobile application development:',
                        '- Architecture design and implementation',
                        '- Security implementation and testing',
                        '- Third-party system integration',
                        '- Performance optimization'
                    ]
                },
                {
                    'category': 'Core Banking & Payment Systems',
                    'description': [
                        'Managing new core banking project implementation:',
                        '- CR2 integration and system migration',
                        '- Card Zone payment switch implementation',
                        '- Interface development with external systems',
                        '- Testing and quality assurance',
                        'Leading critical payment infrastructure projects:',
                        '- MPU New Switch Certification process',
                        '- CR2 Switch migration and optimization',
                        '- POS Acquiring System implementation',
                        '- Merchant integration and onboarding',
                        'Network infrastructure design and implementation:',
                        '- MPU core network architecture',
                        '- Banking network security',
                        '- ATM network optimization',
                        '- International card scheme integration (VISA, Master Card, UPI, JCB)',
                        '- Network redundancy and failover systems'
                    ]
                },
                {
                    'category': 'Infrastructure & Compliance',
                    'description': [
                        'PCI-DSS Compliance Management:',
                        '- Successfully implemented PCI-DSS 3.2.2 and 3.2.3 standards',
                        '- Regular security assessments and audits',
                        '- Compliance documentation and reporting',
                        '- Security control implementation and monitoring',
                        'ATM Infrastructure Management:',
                        '- Implementation of new CDM (Cash Deposit Machine) systems',
                        '- CRM (Cash Recycling Machine) deployment',
                        '- VTM (Virtual Teller Machine) implementation with NCR',
                        '- ATM software and security updates',
                        'Payment Infrastructure:',
                        '- POS terminal network management',
                        '- Card services infrastructure',
                        '- Payment gateway maintenance',
                        '- Network security implementation',
                        'Backend Systems:',
                        '- Tollgate Backend System design and implementation',
                        '- System monitoring and maintenance',
                        '- Performance optimization',
                        '- Disaster recovery planning'
                    ]
                }
            ]
        }
    ]
    
    skills = {
        'Technical': [
            'Payment Systems Architecture',
            'API Integration',
            'Cloud Computing',
            'Database Management',
            'System Security'
        ],
        'Management': [
            'Agile & Scrum',
            'Team Leadership',
            'Project Management',
            'Stakeholder Management',
            'Product Development'
        ],
        'Domain': [
            'Payment Card Industry (PCI)',
            'Digital Banking',
            'Card Payment Systems',
            'Financial Technology',
            'Banking Regulations'
        ]
    }
    
    certifications = [
        {
            'name': 'Project Management Professional (PMP)',
            'issuer': 'Project Management Institute',
            'year': '2024'
        },
        {
            'name': 'Professional Scrum Product Owner (PSPO)',
            'issuer': 'Scrum.org',
            'year': '2023'
        },
        {
            'name': 'Agile SCRUM Master Certified',
            'issuer': 'International Scrum Institute',
            'year': '2023'
        },
        {
            'name': 'SCRUM Master Certified',
            'issuer': 'SCRUMstudy',
            'year': '2022'
        },
        {
            'name': 'PCI-SI (Payment Card Industry – Security Implementer)',
            'issuer': 'PCI Security Standards Council',
            'year': '2023'
        }
    ]
    
    projects = [
        {
            'name': 'Digital Payment Platform',
            'description': 'Led the development and implementation of a comprehensive digital payment solution integrating multiple card schemes',
            'achievements': ['Reduced transaction processing time by 40%', 'Increased system reliability to 99.99%']
        },
        {
            'name': 'Payment Gateway Enhancement',
            'description': 'Spearheaded the upgrade of payment gateway infrastructure to support new payment methods',
            'achievements': ['Integrated 5 new payment schemes', 'Enhanced security protocols']
        }
    ]

    about_info = {
        'name': 'Phyo Minn Thu',
        'title': 'IT and Digital Banking Project Leader',
        'experience': '15+ years',
        'summary': 'I am Phyo Minn Thu, an experienced IT and Digital Banking Project Leader with over 15 years of proven expertise in mobile banking, digital payment systems, card and ATM operations, core banking integrations, and enterprise network infrastructure. With a strong background in managing large-scale financial technology projects at leading banks such as AYA Bank, KBZ Bank, and AGD Bank, I specialize in driving innovation through Agile methodologies, strategic leadership, and cross-functional team collaboration. Certified in PSPO, Scrum Master, PCI Security, AWS Cloud, and Cisco networking, I am passionate about building future-ready digital ecosystems that enhance financial services and customer experiences'
    }

    contact_info = {
        'linkedin': 'https://www.linkedin.com/in/phyo-minn-thu-0555abb2/',
        'email': 'phyominthu.89@gmail.com',
        'phone': '+959798981310'
    }

    return render_template('index.html', 
                         experience=experience,
                         skills=skills,
                         certifications=certifications,
                         projects=projects,
                         contact_info=contact_info,
                         about_info=about_info)

if __name__ == '__main__':
    app.run(debug=True)
