# agent-skills-montry - DigitalNawa Studio

نظام Skills كامل لاستوديو DigitalNawa. 6 مهارات مترابطة، تم بناؤها وفحصها بدون أخطاء.

التثبيت - 30 ثانية

على Claude Code (الأفضل):

cp -r agent-skills-montry/* ~/.claude/skills/
تحقق:
ls ~/.claude/skills/montry
ls ~/.claude/skills/brand-digitalnawa

على Windows:

C:\Users\اسمك.claude\skills\montry
C:\Users\اسمك.claude\skills\brand-digitalnawa
انسخ كل مجلد بنفس الاسم

على Antigravity:

افتح Antigravity > Skills > Import > اختر مجلد agent-skills-montry

طريقة الاستخدام

اكتب فقط:
اعملي فيديو شعار DigitalNawa 9 ثواني
سيقوم montry باستدعاء باقي المهارات بالترتيب الصحيح.

الترتيب الصحيح

montry (المنسق) - دائما أولا

brand-digitalnawa (الهوية) - إجباري قبل أي عمل

hook-analyzer (للفيديوهات أكبر من 15 ثانية)

motion-builder (التنفيذ)

cut-editor (للقص والاختصار)

qc-checker (المراجعة النهائية) - إجباري قبل التسليم

اختبار سريع - بدون أخطاء

اكتب في Claude Code:
استخدم سكيل montry واعملي فيديو شعار DigitalNawa 9 ثواني، واسحب الشعار من GitHub

إذا طلب منك الشعار، هذا صحيح - معناه أن Skill يمنع التخمين. ارفع له ملف الشعار PNG.

الملفات

montry/SKILL.md - المنسق

brand-digitalnawa/SKILL.md - الهوية

hook-analyzer/SKILL.md - الافتتاحيات

cut-editor/SKILL.md - القص

motion-builder/SKILL.md - التنفيذ

qc-checker/SKILL.md - الجودة

ضمان عدم وجود أخطاء

كل ملف SKILL.md يبدأ بـ frontmatter صحيح name + description

كل Skill يمنع التخمين: إذا نقص الشعار أو اللون، يتوقف ويسألك بدل أن يخترع

ترتيب التنفيذ ثابت: Brand أولا، QC أخيرا، لا يمكن تخطيه
