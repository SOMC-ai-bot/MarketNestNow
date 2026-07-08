import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. MarketNestnow - A content Marketing Agency
content = content.replace('<span>MarketNestnow</span>', '<span>MarketNestnow<br><span style="font-size: 0.5em; font-weight: 500; display: block; margin-top: -5px; color: #e0d4ff;">A Content Marketing Agency</span></span>')

# 2. Fix Overlapping Titles (hollow and solid titles)
content = re.sub(r'\.section-header \{([^\}]+)\}', r'.section-header {\1\n      text-align: center;\n      display: flex;\n      flex-direction: column;\n      align-items: center;\n      justify-content: center;\n      height: 120px;\n    }', content)

content = re.sub(r'\.hollow-title \{([^\}]+)top: -40px;([^\}]+)\}', r'.hollow-title {\1top: 10px;\2}', content)

# 3. Services content
services_html = '''
    <div class="services-grid">
      <div class="service-card scroll-anim">
        <h3>Social Media Management</h3>
        <p>Instagram, Linkedin, Facebook, Snapchat, Reddit</p>
      </div>
      <div class="service-card scroll-anim" style="transition-delay: 0.1s;">
        <h3>Youtube Management</h3>
        <p>Full time Management, growth including content creation strategy planning with analytics</p>
      </div>
      <div class="service-card scroll-anim" style="transition-delay: 0.2s;">
        <h3>Graphic Designing</h3>
        <p>Creating Professional Thumbnail for Your all social media and creating caraousel and posts</p>
      </div>
      <div class="service-card scroll-anim" style="transition-delay: 0.3s;">
        <h3>Influencer Marketing</h3>
        <p>Help you to connect with brands or Influencers collab to increase growth (connecting Brands * Creators)</p>
      </div>
    </div>
'''
content = re.sub(r'<div class="services-grid">.*?</div>\s*</section>', services_html + '\n  </section>', content, flags=re.DOTALL)

# 4. Procedure content
procedure_html = '''
    <div class="timeline-container">
      <div class="timeline-node scroll-anim">
        <div class="timeline-card">
          <div class="timeline-header">
            <span class="step-number">01</span>
            <span class="step-title">Brainstorming</span>
          </div>
          <div class="timeline-body">
            Create new viral content ideas to increase ideas growth.
          </div>
        </div>
      </div>
      <div class="timeline-node scroll-anim">
        <div class="timeline-card">
          <div class="timeline-header">
            <span class="step-number">02</span>
            <span class="step-title">Content Creation and Approval</span>
          </div>
          <div class="timeline-body">
            We review the proposed concepts with your team, refining and polishing until the deliverables exceed your expectations.
          </div>
        </div>
      </div>
      <div class="timeline-node scroll-anim">
        <div class="timeline-card">
          <div class="timeline-header">
            <span class="step-number">03</span>
            <span class="step-title">Creative Team</span>
          </div>
          <div class="timeline-body">
            We are a team with professional and experienced social media management, youtube management and graphic designing team with more than 5 years of experirnce in creative field.
          </div>
        </div>
      </div>
    </div>
'''
content = re.sub(r'<div class="timeline-container">.*?</div>\s*</section>', procedure_html + '\n  </section>', content, flags=re.DOTALL)

# Portfolio Title
content = content.replace('<div class="hollow-title">PORTFOLIO</div>', '<div class="hollow-title">OUR WORK</div>')
content = content.replace('<div class="solid-title">OUR WORK</div>', '<div class="solid-title">OUR WORK</div>')

# Portfolio filters
portfolio_filters = '''
    <div class="portfolio-filters scroll-anim">
      <button class="filter-btn active" data-filter="all">All Projects</button>
      <button class="filter-btn" data-filter="graphic">Graphic Designing</button>
      <button class="filter-btn" data-filter="youtube">Youtube Management</button>
      <button class="filter-btn" data-filter="social">Social Media Management</button>
      <button class="filter-btn" data-filter="influencer">Influencer Meet Brands</button>
    </div>
'''
content = re.sub(r'<div class="portfolio-filters scroll-anim">.*?</div>', portfolio_filters, content, flags=re.DOTALL)

# Portfolio grid
portfolio_grid = '''
    <div class="portfolio-grid">
      <div class="portfolio-item scroll-anim" data-category="graphic">
        <img src="images/placeholder-graphic1.jpg" alt="Graphic Design Thumbnail">
        <div class="portfolio-overlay">
          <span class="portfolio-category">Graphic Designing</span>
          <h4 class="portfolio-title">Thumbnail Design</h4>
        </div>
      </div>
      
      <div class="portfolio-item scroll-anim" data-category="youtube" style="transition-delay: 0.1s;">
        <img src="images/placeholder-youtube1.jpg" alt="Youtube Management - Bottomline">
        <div class="portfolio-overlay">
          <span class="portfolio-category">Youtube Management</span>
          <h4 class="portfolio-title">Channel: Bottomline</h4>
        </div>
      </div>

      <div class="portfolio-item scroll-anim" data-category="youtube" style="transition-delay: 0.2s;">
        <img src="images/placeholder-youtube2.jpg" alt="Youtube Management - MaviGadgets">
        <div class="portfolio-overlay">
          <span class="portfolio-category">Youtube Management</span>
          <h4 class="portfolio-title">Channel: MaviGadgets</h4>
        </div>
      </div>

      <div class="portfolio-item scroll-anim" data-category="youtube" style="transition-delay: 0.3s;">
        <img src="images/placeholder-youtube3.jpg" alt="Youtube Management - Asset Wave">
        <div class="portfolio-overlay">
          <span class="portfolio-category">Youtube Management</span>
          <h4 class="portfolio-title">Channel: Asset Wave</h4>
        </div>
      </div>

      <div class="portfolio-item scroll-anim" data-category="social" style="transition-delay: 0.4s;">
        <img src="images/placeholder-social1.jpg" alt="Social Media Management">
        <div class="portfolio-overlay">
          <span class="portfolio-category">Social Media Management</span>
          <h4 class="portfolio-title">Financial.boss</h4>
        </div>
      </div>

      <div class="portfolio-item scroll-anim" data-category="influencer" style="transition-delay: 0.5s;">
        <img src="images/placeholder-influencer1.jpg" alt="Influencer Meet Brands">
        <div class="portfolio-overlay">
          <span class="portfolio-category">Influencer Meet Brands</span>
          <h4 class="portfolio-title">Dot and key.skincare & MamaEarth</h4>
        </div>
      </div>
    </div>
'''
content = re.sub(r'<div class="portfolio-grid">.*?</div>\s*</section>', portfolio_grid + '\n  </section>', content, flags=re.DOTALL)


# Testimonials
content = content.replace('John Doe', 'Mavi Gadgets')
content = content.replace('Founder, TechVision', 'Client')
content = content.replace('Sarah Miller', 'Priya Sharma')
content = content.replace('Alex Lee', 'Rajesh Kumar')
content = content.replace('JD', 'MG')
content = content.replace('SM', 'PS')
content = content.replace('AL', 'RK')


# Contact section
contact_html = '''
  <!-- CONTACT SECTION -->
  <section class="contact-section" id="contact">
    <div class="contact-info scroll-anim">
      <h2>Contact Details</h2>
      <p>Reach out to us directly or fill our contact form to help us understand your needs.</p>

      <div class="contact-details">
        <div class="contact-item">
          <div class="contact-icon">@</div>
          <span>rambogodslg321@gmail.com</span>
        </div>
        <div class="contact-item">
          <div class="contact-icon">📞</div>
          <span>+91-8918109778</span>
        </div>
      </div>
    </div>

    <div class="contact-form-container scroll-anim" style="display:flex; justify-content:center; align-items:center; flex-direction:column; text-align:center;">
      <h3 style="margin-bottom: 20px; font-size: 1.5rem;">Fill our contact form</h3>
      <button class="btn cta-btn submit-btn" style="width: auto; padding: 15px 40px;" onclick="window.open('https://forms.gle/nFwbyJF7Y97j7o7B7', '_blank')">Open Contact Form</button>
    </div>
  </section>
'''
content = re.sub(r'<!-- CONTACT SECTION -->.*?<!-- FOOTER -->', contact_html + '\n  <!-- FOOTER -->', content, flags=re.DOTALL)

# Header CTA
content = content.replace('onclick="document.getElementById(\'contact\').scrollIntoView({behavior: \'smooth\'})"', 'onclick="window.open(\'https://forms.gle/nFwbyJF7Y97j7o7B7\', \'_blank\')"')

# Footer
content = content.replace('We are a high-end digital marketing and content agency dedicated to shaping the digital future of elite brands through data-driven creativity.', 'We are a high-end content marketing and management agency dedicated to grow your social media, youtube content strategy and help you with brand collaboration and many more.')

# Social links
socials_html = '''
        <div class="social-links">
          <a href="#" target="_blank" class="social-icon">
            <svg width="20" height="20" fill="currentColor" viewBox="0 0 24 24"><path d="M19 0h-14c-2.761 0-5 2.239-5 5v14c0 2.761 2.239 5 5 5h14c2.762 0 5-2.239 5-5v-14c0-2.761-2.238-5-5-5zm-11 19h-3v-11h3v11zm-1.5-12.268c-.966 0-1.75-.79-1.75-1.764s.784-1.764 1.75-1.764 1.75.79 1.75 1.764-.783 1.764-1.75 1.764zm13.5 12.268h-3v-5.604c0-3.368-4-3.113-4 0v5.604h-3v-11h3v1.765c1.396-2.586 7-2.777 7 2.476v6.759z"/></svg>
          </a>
          <a href="#" target="_blank" class="social-icon">
            <svg width="20" height="20" fill="currentColor" viewBox="0 0 24 24"><path d="M12 2.163c3.204 0 3.584.012 4.85.07 3.252.148 4.771 1.691 4.919 4.919.058 1.265.069 1.645.069 4.849 0 3.205-.012 3.584-.069 4.849-.149 3.225-1.664 4.771-4.919 4.919-1.266.058-1.644.07-4.85.07-3.204 0-3.584-.012-4.849-.07-3.26-.149-4.771-1.699-4.919-4.92-.058-1.265-.07-1.644-.07-4.849 0-3.204.013-3.583.07-4.849.149-3.227 1.664-4.771 4.919-4.919 1.266-.057 1.645-.069 4.849-.069zm0-2.163c-3.259 0-3.667.014-4.947.072-4.358.2-6.78 2.618-6.98 6.98-.059 1.281-.073 1.689-.073 4.948 0 3.259.014 3.668.072 4.948.2 4.358 2.618 6.78 6.98 6.98 1.281.058 1.689.072 4.948.072 3.259 0 3.668-.014 4.948-.072 4.354-.2 6.782-2.618 6.979-6.98.059-1.28.073-1.689.073-4.948 0-3.259-.014-3.667-.072-4.947-.196-4.354-2.617-6.78-6.979-6.98-1.281-.059-1.69-.073-4.949-.073zm0 5.838c-3.403 0-6.162 2.759-6.162 6.162s2.759 6.163 6.162 6.163 6.162-2.759 6.162-6.163c0-3.403-2.759-6.162-6.162-6.162zm0 10.162c-2.209 0-4-1.79-4-4 0-2.209 1.791-4 4-4s4 1.791 4 4c0 2.21-1.791 4-4 4zm6.406-11.845c-.796 0-1.441.645-1.441 1.44s.645 1.44 1.441 1.44c.795 0 1.439-.645 1.439-1.44s-.644-1.44-1.439-1.44z"/></svg>
          </a>
          <a href="#" target="_blank" class="social-icon">
            <svg width="20" height="20" fill="currentColor" viewBox="0 0 24 24"><path d="M24 4.557c-.883.392-1.832.656-2.828.775 1.017-.609 1.798-1.574 2.165-2.724-.951.564-2.005.974-3.127 1.195-.897-.957-2.178-1.555-3.594-1.555-3.179 0-5.515 2.966-4.797 6.045-4.091-.205-7.719-2.165-10.148-5.144-1.29 2.213-.669 5.108 1.523 6.574-.806-.026-1.566-.247-2.229-.616-.054 2.281 1.581 4.415 3.949 4.89-.693.188-1.452.232-2.224.084.626 1.956 2.444 3.379 4.6 3.419-2.07 1.623-4.678 2.348-7.29 2.04 2.179 1.397 4.768 2.212 7.548 2.212 9.142 0 14.307-7.721 13.995-14.646.962-.695 1.797-1.562 2.457-2.549z"/></svg>
          </a>
        </div>
'''
content = re.sub(r'<div class="social-links">.*?</div>', socials_html, content, flags=re.DOTALL)

# Button CSS replacements
css_nav = '''
    .nav-links a {
      color: var(--text-main);
      text-decoration: none;
      font-weight: 500;
      font-size: 0.95rem;
      position: relative;
      transition: all 0.3s;
      padding: 8px 16px;
      border-radius: 8px;
      border: 1px solid transparent;
    }

    .nav-links a:hover {
      background: #ffffff;
      color: #000000;
      border: 1px solid #000000;
    }
'''
content = re.sub(r'\.nav-links a \{[^\}]+\}\s*\.nav-links a::after \{[^\}]+\}\s*\.nav-links a:hover::after \{[^\}]+\}\s*\.nav-links a:hover \{[^\}]+\}', css_nav, content, flags=re.DOTALL)

css_btn = '''
    .btn {
      padding: 16px 32px;
      border-radius: 50px;
      font-family: 'Poppins', sans-serif;
      font-weight: 600;
      font-size: 1rem;
      cursor: pointer;
      transition: all 0.3s;
      text-decoration: none;
      display: inline-flex;
      align-items: center;
      justify-content: center;
      border: 1px solid transparent;
    }

    .btn:hover {
      background: #ffffff;
      color: #000000;
      border: 1px solid #000000;
    }

    .btn-primary {
      background: var(--primary-gradient);
      color: var(--surface-white);
    }

    .btn-secondary {
      background: transparent;
      color: var(--surface-white);
      border: 1px solid rgba(255, 255, 255, 0.3);
    }
    
    .cta-btn:hover {
      background: #ffffff;
      color: #000000;
      border: 1px solid #000000;
      transform: translateY(-2px);
      box-shadow: 0 8px 25px rgba(112, 0, 255, 0.6);
    }
'''
content = re.sub(r'\.btn \{[^\}]+\}\s*\.btn-primary \{[^\}]+\}\s*\.btn-primary:hover \{[^\}]+\}\s*\.btn-secondary \{[^\}]+\}\s*\.btn-secondary:hover \{[^\}]+\}', css_btn, content, flags=re.DOTALL)


with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("done")
