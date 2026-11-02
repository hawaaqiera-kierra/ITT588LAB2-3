from django.shortcuts import render


def home(request):
    steps = [
        ("Get to safety", "If you can, move to a safe place or a trusted person's home."),
        ("Call for help", "Call 999 in an emergency, or Talian Kasih 15999 for support."),
        ("Keep evidence", "Save messages, photos, medical reports and dates in a safe place."),
        ("Report it", "Lodge a police report or get help at a hospital One Stop Crisis Centre."),
    ]
    return render(request, 'pages/home.html', {'steps': steps})


def what_is(request):
    definition = (
        "Gender-Based Violence (GBV) is harm directed at a person because of "
        "their gender. It can happen at home, at work, in public spaces or "
        "online. It affects women and girls most, but men, boys and "
        "gender-diverse people can also be victims."
    )
    types = [
        {"title": "Physical violence", "icon": "bi-bandaid",
         "desc": "Hitting, choking, burning or any act that causes bodily harm."},
        {"title": "Sexual violence", "icon": "bi-shield-exclamation",
         "desc": "Rape, sexual assault and any sexual act without consent."},
        {"title": "Sexual harassment", "icon": "bi-chat-left-dots",
         "desc": "Unwelcome sexual remarks, gestures or advances at work, school or in public."},
        {"title": "Psychological abuse", "icon": "bi-cloud-lightning-rain",
         "desc": "Threats, intimidation, humiliation and controlling behaviour."},
        {"title": "Economic abuse", "icon": "bi-cash-coin",
         "desc": "Controlling money, or preventing someone from working or studying."},
        {"title": "Online / cyber violence", "icon": "bi-phone",
         "desc": "Cyberstalking, sharing intimate images without consent, online threats."},
        {"title": "Stalking", "icon": "bi-eye",
         "desc": "Repeated, unwanted following, monitoring or contact."},
        {"title": "Harmful practices", "icon": "bi-slash-circle",
         "desc": "Child marriage and other practices that harm girls and women."},
    ]
    return render(request, 'pages/what_is.html',
                  {'definition': definition, 'types': types})


def law_enforcement(request):
    laws = [
        {"title": "Anti-Sexual Harassment Act 2022 (Act 840)", "icon": "bi-megaphone",
         "desc": "Created the Tribunal for Anti-Sexual Harassment (TAGS) so victims can seek redress."},
        {"title": "Penal Code", "icon": "bi-book",
         "desc": "Covers rape, outrage of modesty, assault, criminal intimidation and related offences."},
        {"title": "Domestic Violence Act 1994", "icon": "bi-house-heart",
         "desc": "Allows victims to apply for Protection Orders when violence happens within the household."},
        {"title": "Sexual Offences Against Children Act 2017", "icon": "bi-shield-check",
         "desc": "Protects children from sexual crimes."},
        {"title": "Communications and Multimedia Act 1998", "icon": "bi-wifi",
         "desc": "Applies to offensive or threatening online communication."},
    ]
    return render(request, 'pages/law_enforcement.html', {'laws': laws})


def enforcer(request):
    agencies = [
        {"title": "Royal Malaysia Police (PDRM) - D11", "icon": "bi-shield-shaded",
         "desc": "Investigates sexual, women and child crimes. Reports can be lodged at any police station."},
        {"title": "Department of Social Welfare (JKM)", "icon": "bi-house-heart",
         "desc": "Protection Officers, shelters and counselling."},
        {"title": "Tribunal for Anti-Sexual Harassment (TAGS)", "icon": "bi-bank",
         "desc": "Hears sexual harassment complaints under Act 840."},
        {"title": "Ministry of Women, Family and Community Development (KPWKM)", "icon": "bi-people",
         "desc": "Policy, programmes and support services for women and families."},
        {"title": "One Stop Crisis Centre (OSCC) - Government Hospitals", "icon": "bi-hospital",
         "desc": "Medical care, police report and counselling in one location."},
        {"title": "Legal Aid Department (JBG)", "icon": "bi-journal-check",
         "desc": "Legal advice and representation."},
        {"title": "Malaysian Communications and Multimedia Commission (MCMC)", "icon": "bi-wifi",
         "desc": "Handles complaints about harmful online content."},
    ]
    return render(request, 'pages/enforcer.html', {'agencies': agencies})


def hotline(request):
    hotlines = [
        {"name": "Emergency (Police)", "icon": "bi-exclamation-octagon", "urgent": True,
         "display": "999", "tel": "999", "whatsapp": "",
         "desc": "Immediate danger. From a mobile you can also dial 112."},
        {"name": "Talian Kasih (JKM)", "icon": "bi-telephone-fill", "urgent": False,
         "display": "15999", "tel": "15999", "whatsapp": "60192615999",
         "desc": "National helpline for abuse and welfare. WhatsApp: 019-261 5999."},
        {"name": "WAO Hotline", "icon": "bi-heart-fill", "urgent": False,
         "display": "03-3000 8858", "tel": "+60330008858", "whatsapp": "60189888058",
         "desc": "Support from Women's Aid Organisation. WhatsApp: 018-988 8058."},
        {"name": "Befrienders KL", "icon": "bi-chat-heart-fill", "urgent": False,
         "display": "03-7627 2929", "tel": "+60376272929", "whatsapp": "",
         "desc": "Emotional support for anyone who needs someone to talk to."},
    ]
    return render(request, 'pages/hotline.html', {'hotlines': hotlines})


def contact(request):
    sent = False
    if request.method == 'POST':
        # Demo only: a real site would save or email this message.
        sent = True
    return render(request, 'pages/contact.html', {'sent': sent})

def safety_check(request):
    return render(request, 'pages/safety_check.html')