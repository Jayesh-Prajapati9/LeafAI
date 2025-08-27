# LeafAI 🌿

## Introduction 🚀

LeafAI is a cutting-edge artificial intelligence solution designed to revolutionize plant disease detection and management. Built with farmers, agricultural researchers, and plant enthusiasts in mind, this web-based platform leverages the power of deep learning to provide instant, accurate identification of plant diseases from simple leaf photographs.

### Why LeafAI? 🤔

- **Early Detection:** Identify plant diseases at their earliest stages, enabling prompt intervention and reducing crop losses
- **Accessibility:** No specialized equipment needed - just a smartphone camera or digital photo
- **Cost-Effective:** Reduces the need for expensive laboratory testing and expert consultations
- **Educational:** Helps users learn about various plant diseases and their characteristics
- **Data-Driven:** Contributes to a growing database of plant disease information for research purposes

### Impact & Vision 🎯

LeafAI aims to:
- Reduce global crop losses due to diseases
- Empower farmers with accessible technology
- Promote sustainable farming practices
- Create a comprehensive plant disease database
- Support agricultural research and education

## Features ✨

### Core Functionality
- 🌿 **Smart Upload:** Drag-and-drop or click to upload plant images
- 🤖 **AI Analysis:** Powered by MobileNetV2 with 96% accuracy
- 📊 **Detailed Reports:** Get comprehensive disease information
- 💡 **Treatment Suggestions:** Receive actionable recommendations
- 📱 **Mobile-First:** Responsive design for field use

### User Features
- 🔒 **Secure Authentication:** Protected user accounts
- 📁 **History Tracking:** Save and review past analyses
- 📈 **Analytics Dashboard:** Track disease patterns
- 🌍 **Community Features:** Share and discuss findings
- 📱 **Progressive Web App:** Install on mobile devices

## Technology Stack 🛠

### Backend
- **Framework:** Django 5.2
- **API:** Django REST Framework
- **Database:** SQLite3 (Development) / PostgreSQL (Production)
- **Authentication:** Django Allauth

### Frontend
- **Styling:** TailwindCSS

### AI/ML
- **Framework:** TensorFlow
- **Model:** MobileNetV2
- **Training:** Transfer Learning
- **Dataset:** PlantVillage (50,000+ images)

## Project Structure 📁

```
LeafAI/
├── 📁 accounts/          # User authentication
├── 📁 dashboard/         # User dashboard
├── 📁 LeafAI/           # Project settings
├── 📁 media/            # User uploads
├── 📁 pages/            # Static pages
├── 📁 prediction/        # Disease prediction
├── 📁 Mobile_Net_V2/    # AI model files
│   ├── 📄 model.h5
│   └── 📄 labels.pkl
└── 📁 templates/        # HTML templates
```

## Installation Guide 📥

### Prerequisites
```bash
Python 3.10+
pip (latest)
Git
Virtual environment
```

### Setup Steps

1. **Clone Repository:**
```bash
git clone https://github.com/yourusername/LeafAI.git
cd LeafAI
```

2. **Create Virtual Environment:**
```bash
python -m venv venv
.\venv\Scripts\activate
```

3. **Install Dependencies:**
```bash
pip install -r requirements.txt
```

4. **Environment Setup:**
```bash
cp .env.example .env
# Edit .env with your settings
```

5. **Database Setup:**
```bash
python manage.py migrate
python manage.py createsuperuser
```

6. **Run Development Server:**
```bash
python manage.py runserver
```

## Usage Guide 📘

1. **Account Creation**
   - Register at `/accounts/register`
   - Verify email
   - Complete profile

2. **Image Upload**
   - Select clear, well-lit leaf images
   - Center the affected area
   - Multiple angles recommended

3. **Analysis**
   - Review AI predictions
   - Check confidence scores
   - View detailed disease information

4. **Dashboard**
   - Track analysis history
   - Download reports
   - Monitor trends

## Contributing 🤝

1. Fork the repository
2. Create feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit changes (`git commit -m 'Add AmazingFeature'`)
4. Push to branch (`git push origin feature/AmazingFeature`)
5. Open Pull Request

## Testing 🧪

Run tests with:
```bash
python manage.py test
```

For coverage report:
```bash
coverage run manage.py test
coverage report
```

## Acknowledgements 🙏

- PlantVillage Dataset Team
- TensorFlow Community
- Django Framework
- Open Source Contributors

Built with ❤️ for sustainable