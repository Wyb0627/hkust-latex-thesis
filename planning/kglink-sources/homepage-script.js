document.addEventListener('DOMContentLoaded', function() {
    // Function to load content from files
    async function loadContent(sectionId, texFile) {
        try {
            const response = await fetch(texFile);
            const content = await response.text();
            document.getElementById(sectionId + '-content').innerHTML = content;
        } catch (error) {
            console.error(`Error loading ${texFile}:`, error);
            document.getElementById(sectionId + '-content').innerHTML = 
                '<p>Error loading content. Please try again later.</p>';
        }
    }

    // Load content for each section
    const sections = {
        'about-me': 'about me.tex',
        'education': 'education.tex',
        'internship-experience': 'internship experience.tex',
        'research-interest': 'research interest.tex',
        'publications': 'publications.tex',
        'other-publications': 'other_pub.tex',
        'teaching': 'teaching.tex',
        'services': 'services.tex'
    };

    // Load all sections
    for (const [sectionId, texFile] of Object.entries(sections)) {
        loadContent(sectionId, texFile);
    }

    // Add smooth scrolling for navigation
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            const target = document.querySelector(this.getAttribute('href'));
            if (target) {
                target.scrollIntoView({
                    behavior: 'smooth',
                    block: 'start'
                });
            }
        });
    });
}); 
