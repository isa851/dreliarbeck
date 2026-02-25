from django.core.management.base import BaseCommand
from apps.pages.models import (
    HomePage, HomeFeature, HomeStat, Service, DoctorProfile, 
    DoctorFact, Case, Review, SiteSettings, AppointmentRequest
)
from django.utils import timezone
from datetime import date

class Command(BaseCommand):
    help = 'Create sample data for the dental clinic website'

    def handle(self, *args, **options):
        self.stdout.write('Creating sample data...')
        
        # Create site settings
        site_settings = SiteSettings.objects.create(
            brand_name="Dr. Eliyar",
            phone="+996 (555) 12-34-56",
            email="info@dreliar.kg",
            address="г. Бишкек, ул. Киевская 77",
            work_time="Пн-Пт: 09:00-20:00, Сб: 10:00-18:00",
            instagram="https://instagram.com/dreliar",
            telegram="https://t.me/dreliar",
            whatsapp="https://wa.me/996555123456"
        )
        
        # Create home page
        home = HomePage.objects.create(
            hero_badge="Приём открыт",
            hero_title="Стоматология\nнового поколения",
            hero_subtitle="Виниры, имплантация и лечение без боли — с заботой о каждой детали вашей улыбки. Клиника Dr. Eliyar в Бишкеке.",
            hero_calm_text="Мы знаем, что визит к стоматологу — это стресс. Именно поэтому мы делаем всё, чтобы вам было комфортно и спокойно на каждом этапе.",
            trust_title="Почему нам доверяют",
            trust_subtitle="Каждый пациент для нас — не просто приём, а история, которой мы гордимся",
            services_title="Наши услуги",
            services_subtitle="Комплексный подход к здоровью и красоте вашей улыбки",
            team_title="Наша команда",
            team_subtitle="Профессионалы, которым вы доверяете свою улыбку",
            tour_title="Загляните в клинику",
            tour_subtitle="Познакомьтесь с нашими кабинетами, оборудованием и зоной отдыха, не выходя из дома. Виртуальный тур поможет вам чувствовать себя увереннее перед первым визитом.",
            tour_calm_text="Особенно рекомендуем тем, кто нервничает — знакомое пространство снижает тревогу.",
            doctor_title="Dr. Eliyar",
            doctor_subtitle="Более 12 лет клинического опыта. Обучался в Германии и Южной Корее. Специализация — эстетическая реставрация и дентальная имплантация. Каждый случай рассматривает индивидуально.",
            cases_title="Результаты работы",
            cases_subtitle="Реальные кейсы наших пациентов — до и после",
            reviews_title="Что говорят пациенты",
            reviews_subtitle="Отзывы наших пациентов — лучшая рекомендация",
            cta_title="Запишитесь на бесплатную консультацию",
            cta_subtitle="Узнайте план лечения и точную стоимость — без обязательств",
            cta_calm_text="Если вы боитесь — просто скажите. Мы подготовимся и всё пройдёт максимально комфортно."
        )
        
        # Create trust features
        trust_features = [
            {
                "title": "12 лет опыта",
                "text": "Более 5 000 довольных пациентов. Каждый кейс — результат глубокой экспертизы и внимания к деталям.",
                "icon": "fa-trophy"
            },
            {
                "title": "Современное оборудование",
                "text": "3D-томограф, дентальный микроскоп, лазер — мы используем технологии, которые делают лечение точнее и безболезненнее.",
                "icon": "fa-microscope"
            },
            {
                "title": "Премиум-материалы",
                "text": "Работаем только с немецкими и швейцарскими брендами: Straumann, E-max, Ivoclar. Гарантия качества от 5 лет.",
                "icon": "fa-gem"
            },
            {
                "title": "Честная стоимость",
                "text": "Фиксированные цены без скрытых доплат. Вы знаете итоговую сумму ещё до начала лечения.",
                "icon": "fa-handshake"
            }
        ]
        
        for i, feature_data in enumerate(trust_features):
            HomeFeature.objects.create(
                home=home,
                title=feature_data["title"],
                text=feature_data["text"],
                icon=feature_data["icon"],
                order=i
            )
        
        # Create stats for doctor
        stats = [
            {"value": "5 000+", "label": "пациентов"},
            {"value": "12", "label": "лет опыта"},
            {"value": "15+", "label": "курсов"}
        ]
        
        for i, stat_data in enumerate(stats):
            HomeStat.objects.create(
                home=home,
                value=stat_data["value"],
                label=stat_data["label"],
                order=i
            )
        
        # Create services
        services = [
            {
                "title": "Имплантация",
                "description": "Восстановление зубов на имплантатах Straumann с пожизненной гарантией. Безболезненная операция с навигационным шаблоном.",
                "price_from": 150000,
                "currency": "сом",
                "icon": "fa-tooth"
            },
            {
                "title": "Виниры E-max",
                "description": "Тончайшие керамические накладки, которые создают идеальную улыбку. Минимальная обточка, максимальный результат.",
                "price_from": 25000,
                "currency": "сом",
                "icon": "fa-smile"
            },
            {
                "title": "Лечение под микроскопом",
                "description": "Лечение кариеса и пульпита с увеличением в 25х. Точность до микрона — сохраняем максимум здоровой ткани.",
                "price_from": 8000,
                "currency": "сом",
                "icon": "fa-microscope"
            }
        ]
        
        for i, service_data in enumerate(services):
            Service.objects.create(
                title=service_data["title"],
                description=service_data["description"],
                price_from=service_data["price_from"],
                currency=service_data["currency"],
                icon=service_data["icon"],
                order=i
            )
        
        # Create doctors
        doctors = [
            {
                "name": "Dr. Eliyar",
                "role": "Главный врач · Ортопед · Имплантолог",
                "description": "12 лет опыта. Обучался в Германии и Южной Корее. Специализация — эстетика и имплантация."
            },
            {
                "name": "Dr. Айгерим",
                "role": "Стоматолог-терапевт",
                "description": "8 лет опыта. Специализация — лечение под микроскопом, художественная реставрация."
            },
            {
                "name": "Dr. Бекзат",
                "role": "Хирург · Имплантолог",
                "description": "10 лет опыта. Навигационная имплантация, удаление зубов мудрости. Стажировка в Турции."
            },
            {
                "name": "Dr. Нуржан",
                "role": "Ортодонт",
                "description": "6 лет опыта. Элайнеры, брекеты, исправление прикуса. Сертифицированный специалист Invisalign."
            }
        ]
        
        for i, doctor_data in enumerate(doctors):
            doctor = DoctorProfile.objects.create(
                name=doctor_data["name"],
                role=doctor_data["role"],
                description=doctor_data["description"],
                order=i
            )
        
        # Create cases
        cases = [
            {
                "title": "Полная эстетическая реставрация",
                "description": "10 виниров E-max. Срок — 2 недели.",
                "tag": "Виниры",
                "duration": "2 недели"
            },
            {
                "title": "Восстановление жевательных зубов",
                "description": "3 имплантата Straumann. Срок — 3 месяца.",
                "tag": "Имплантация",
                "duration": "3 месяца"
            },
            {
                "title": "Zoom-отбеливание на 6 тонов",
                "description": "Профчистка + отбеливание за 1 день.",
                "tag": "Отбеливание",
                "duration": "1 день"
            }
        ]
        
        for i, case_data in enumerate(cases):
            Case.objects.create(
                title=case_data["title"],
                description=case_data["description"],
                tag=case_data["tag"],
                duration=case_data["duration"],
                order=i
            )
        
        # Create reviews
        reviews = [
            {
                "text": "Впервые не боялась идти к стоматологу! Доктор Элияр всё объяснил, процедура прошла безболезненно. Результат — идеальная улыбка!",
                "author_name": "Айгуль К.",
                "rating": 5
            },
            {
                "text": "Делал имплантацию — качество на высшем уровне. Клиника оснащена по последнему слову техники. Спасибо за новую улыбку!",
                "author_name": "Марат Т.",
                "rating": 5
            },
            {
                "text": "Виниры — просто космос! Очень приятная атмосфера, вежливый персонал. Рекомендую всем знакомым!",
                "author_name": "Дана С.",
                "rating": 5
            }
        ]
        
        for i, review_data in enumerate(reviews):
            Review.objects.create(
                text=review_data["text"],
                author_name=review_data["author_name"],
                rating=review_data["rating"],
                order=i
            )
        
        self.stdout.write(self.style.SUCCESS('Sample data created successfully!'))
