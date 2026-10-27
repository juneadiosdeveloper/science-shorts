# Idea source: warikoo "30,000 vs 3,00,000 vs 3,00,00,000 INR Per Month" (~1.2M views). Our own script and numbers.
# Numbers (Python, monthly SIP at start of month, r/12, step-up every 12 months, 25 yr @12% assumed):
#   dost ₹7,500 +10%/yr → ₹3.21 cr (invested ₹88.5 lakh); Chintu ₹15,000 flat → ₹2.85 cr (invested ₹45 lakh)
LINES = [
 (1,"L","तीस हज़ार की सैलरी वाला, तीन लाख वाले से ज़्यादा अमीर? सुनो चिंटू की कहानी!",[("₹30,000 vs ₹3 LAKH","white"),("KAUN ZYADA AMEER?","gold")],"s01"),
 (2,"G","मेरी सैलरी तीन लाख! मेरा दोस्त सिर्फ़ तीस हज़ार कमाता है। मैं तो दस गुना अमीर बनूँगा!",[("CHINTU: ₹3 LAKH/MAHINA","white")],"s02"),
 (3,"P","दोस्त हर महीने साढ़े सात हज़ार बचाता है, और हर साल उसे दस प्रतिशत बढ़ाता है।",[("DOST: ₹7,500 SIP","white"),("+10% HAR SAAL","gold")],"s03"),
 (4,"G","मैं तो पंद्रह हज़ार बचाता हूँ, पूरे दुगने! बाकी सब ई एम आई और शौक में।",[("CHINTU: ₹15,000 SIP","white"),("KABHI NAHI BADHAYA","red")],"s04"),
 (5,"P","पर तुम्हारी बचत कभी नहीं बढ़ी। पच्चीस साल, बारह प्रतिशत मानकर... तुम्हारे बनते हैं लगभग दो करोड़ पचासी लाख।",[("CHINTU, 25 SAAL BAAD","white"),("~₹2.85 CRORE","gold")],"s05"),
 (6,"P","और दोस्त के? लगभग तीन करोड़ इक्कीस लाख!",[("DOST: ~₹3.21 CRORE","gold")],"s06"),
 (7,"G","दस गुना सैलरी... और पैसा कम?!",[("10x SALARY, KAM PAISA?!","red")],"s07"),
 (8,"P","अमीरी सैलरी से नहीं, हर साल बचत बढ़ाने की आदत से आती है। आप सैलरी का कितना प्रतिशत बचाते हो? कमेंट करो!",[("SALARY ≠ AMEERI","gold"),("COMMENT KARO","white")],"s08"),
]
