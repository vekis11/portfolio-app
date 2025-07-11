# VekisTech Portfolio

Professional portfolio website for VekisTech - Cloud & DevOps Expert, deployed on GitHub Pages with custom domain.

## 🌐 Live Site
Visit: [https://vekistech.pro](https://vekistech.pro)

## 🚀 Features
- **Custom Domain**: Configured with `vekistech.pro`
- **Responsive Design**: Modern, mobile-friendly interface
- **Static Site**: Built with Jekyll for GitHub Pages
- **Professional Portfolio**: Showcasing cloud and DevOps expertise

## 📁 Project Structure
```
portfolio-app/
├── index.html              # Homepage
├── contact.html            # Contact page
├── projects.html           # Projects showcase
├── certifications.html     # Professional certifications
├── testimonials.html       # Client testimonials
├── job-support.html        # Services offered
├── CNAME                   # Custom domain configuration
├── _config.yml            # Jekyll configuration
├── Gemfile                # Ruby dependencies
└── .github/workflows/     # GitHub Actions workflows
```

## 🛠️ Technology Stack
- **Frontend**: HTML5, CSS3, Bootstrap 5, JavaScript
- **Build Tool**: Jekyll (GitHub Pages)
- **Deployment**: GitHub Pages with custom domain
- **Styling**: Custom CSS with gradient backgrounds and animations

## 🔧 Setup Instructions

### 1. Repository Setup
- Ensure your repository is public (required for GitHub Pages)
- Push all files to the `main` branch

### 2. GitHub Pages Configuration
1. Go to your repository Settings
2. Navigate to "Pages" in the sidebar
3. Set Source to "GitHub Actions"
4. Ensure the repository is public

### 3. Custom Domain Configuration
The `CNAME` file is already configured with `vekistech.pro`

### 4. DNS Configuration
Configure your DNS provider with the following records:

#### For GitHub Pages:
- **Type**: CNAME
- **Name**: @ (or your domain)
- **Value**: `yourusername.github.io`

#### For www subdomain:
- **Type**: CNAME
- **Name**: www
- **Value**: `yourusername.github.io`

### 5. Deployment
The site will automatically deploy when you push to the `main` branch. The GitHub Actions workflow will:
1. Build the Jekyll site
2. Deploy to GitHub Pages
3. Configure the custom domain

## 📝 Content Management
- Update content by editing the HTML files directly
- Images can be added to the repository and referenced
- Contact form uses `mailto:` links (consider integrating with a form service)

## 🎨 Customization
- Colors and styling can be modified in the CSS sections of each HTML file
- The gradient background uses CSS variables for easy customization
- Font is set to Poppins from Google Fonts

## 🔒 Security
- HTTPS is automatically enabled by GitHub Pages
- No sensitive data is stored in the repository
- Contact form uses client-side email links

## 📞 Support
For questions or issues with the deployment, check:
1. GitHub Pages documentation
2. Jekyll documentation
3. Your DNS provider's documentation

---

**Built with ❤️ for VekisTech**