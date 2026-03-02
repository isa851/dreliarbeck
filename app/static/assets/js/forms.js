/**
 * Dr. Eliyar — Chat Form with Django POST
 */

console.log("CHAT JS LOADED");

document.addEventListener('DOMContentLoaded', () => {

    const chatBody = document.getElementById('chatBody');
    const chatInputArea = document.getElementById('chatInputArea');
    const chatInput = document.getElementById('chatInput');
    const chatSendBtn = document.getElementById('chatSendBtn');

    if (!chatBody) return;

    const steps = [
        {
            bot: 'Здравствуйте! 👋 Я помогу вам записаться. Что вас беспокоит?',
            options: ['Болит зуб', 'Хочу виниры', 'Имплантация', 'Чистка зубов', 'Другое']
        },
        {
            bot: 'Отлично! Когда вам удобно прийти?',
            options: ['Ближайшие дни', 'На этой неделе', 'На следующей неделе', 'Свой вариант']
        },
        {
            bot: 'Скажите, вы боитесь стоматолога?',
            options: ['Да, немного боюсь', 'Нет, всё ок']
        },
        {
            bot: 'Как вас зовут?',
            input: true,
            placeholder: 'Ваше имя'
        },
        {
            bot: 'Ваш номер телефона:',
            input: true,
            placeholder: '+996 ___ ___ ___'
        }
    ];

    let currentStep = 0;
    const userAnswers = [];

    function addMessage(text, type) {
        const msg = document.createElement('div');
        msg.className = `chat__msg chat__msg--${type}`;
        msg.textContent = text;
        chatBody.appendChild(msg);
        chatBody.scrollTop = chatBody.scrollHeight;
    }

    function nextStep() {
        currentStep++;

        if (currentStep >= steps.length) {
            finishChat();
        } else {
            setTimeout(showStep, 400);
        }
    }

    function addOptions(options) {
        const wrap = document.createElement('div');
        wrap.className = 'chat__options';

        options.forEach(opt => {
            const btn = document.createElement('button');
            btn.className = 'chat__option-btn';
            btn.textContent = opt;

            btn.addEventListener('click', () => {
                addMessage(opt, 'user');
                userAnswers.push(opt);
                wrap.remove();
                nextStep();
            });

            wrap.appendChild(btn);
        });

        chatBody.appendChild(wrap);
        chatBody.scrollTop = chatBody.scrollHeight;
    }

    function showStep() {
        const step = steps[currentStep];
        addMessage(step.bot, 'bot');

        if (step.options) {
            setTimeout(() => addOptions(step.options), 300);
            chatInputArea.style.display = 'none';
        }

        if (step.input) {
            chatInputArea.style.display = 'flex';
            chatInput.placeholder = step.placeholder;
            chatInput.value = '';
            chatInput.focus();
        }
    }

    function handleInputSend() {
        const value = chatInput.value.trim();
        if (!value) return;

        addMessage(value, 'user');
        userAnswers.push(value);

        chatInput.value = '';
        chatInputArea.style.display = 'none';

        nextStep();
    }

    function finishChat() {

        const payload = {
            problem: userAnswers[0] || '',
            date: userAnswers[1] || '',
            fear: userAnswers[2] || '',
            name: userAnswers[3] || '',
            phone: userAnswers[4] || ''
        };

        fetch("/api/chat-booking/", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify(payload)
        })
        .then(res => res.json())
        .then(data => {
            if (data.success) {
                addMessage("✅ Спасибо! Мы получили вашу заявку. Скоро свяжемся с вами.", "bot");
            } else {
                addMessage("❌ Ошибка отправки. Попробуйте позже.", "bot");
                console.log(data);
            }
        })
        .catch(err => {
            console.error(err);
            addMessage("❌ Ошибка соединения с сервером.", "bot");
        });
    }

    if (chatSendBtn) {
        chatSendBtn.addEventListener('click', handleInputSend);
    }

    if (chatInput) {
        chatInput.addEventListener('keydown', (e) => {
            if (e.key === 'Enter') {
                handleInputSend();
            }
        });
    }

    // старт чата
    setTimeout(showStep, 600);
});

/* ============================= */
/* BOOKING FORM (Contacts page) */
/* ============================= */

document.addEventListener("DOMContentLoaded", function () {

    const bookingForm = document.getElementById("bookingForm");
    if (!bookingForm) return;

    console.log("BOOKING FORM CONNECTED");

    bookingForm.addEventListener("submit", function (e) {
        e.preventDefault();

        const name = document.getElementById("bookName").value.trim();
        const phone = document.getElementById("bookPhone").value.trim();
        const service = document.getElementById("bookService").value;
        const comment = document.getElementById("bookComment").value.trim();

        if (!name || !phone) {
            alert("Введите имя и телефон");
            return;
        }

        fetch("/api/booking/", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify({
                name: name,
                phone: phone,
                service: service,
                comment: comment
            })
        })
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                alert("✅ Заявка успешно отправлена!");
                bookingForm.reset();
            } else {
                alert("❌ Ошибка отправки");
                console.log(data);
            }
        })
        .catch(error => {
            console.error(error);
            alert("❌ Ошибка соединения с сервером");
        });
    });

});