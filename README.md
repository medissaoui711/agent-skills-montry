# DigitalNawa Studio

مستودع Plugin لاستوديو إنتاج فيديو يعتمد مهارات متخصصة وعقود بيانات قابلة للتحقق، مع Remotion كمحرك الإنتاج الأساسي.

> **تنبيه الحالة:** الهوية البصرية الرسمية ما زالت قيد التحقق. لا تستخدم ألواناً أو خطوطاً أو شعارات من النسخ القديمة بوصفها معتمدة قبل اعتماد Brand Contract.

## المكونات

- `montry`: تنسيق سير العمل وتحديد المهارات المطلوبة.
- `brand-digitalnawa`: التحقق من مصدر الهوية وإعداد Brand Contract.
- `hook-analyzer`: تحليل الافتتاحية عند الحاجة السردية.
- `cut-editor`: إعداد قرارات القص من المواد الخام.
- `motion-builder`: إعداد Production Plan.
- `remotion-engine`: معاينة وتنفيذ خطة الإنتاج باستخدام Remotion.
- `qc-checker`: فحص قائم على الأدلة.
- `contracts/`: سبعة JSON Schemas للعقود بين المراحل.

## تثبيت Claude Code

### تشغيل المستودع كـ Plugin محلياً

من نسخة المستودع المحلية:

```bash
claude --plugin-dir ./agent-skills-montry
```

استبدل المسار بمسار المستودع الفعلي. هذا أسلوب تطوير محلي؛ اتبع واجهة Plugin Manager في Claude Code للتثبيت الدائم.

### تثبيت المهارات يدوياً

إذا كنت تريد تثبيت المهارات بدلاً من Plugin، انسخ المجلدات الموجودة داخل `skills/` فقط:

```bash
mkdir -p ~/.claude/skills
cp -R skills/* ~/.claude/skills/
```

لا تنسخ مجلدات الجذر القديمة؛ مصدر المهارات النشط هو `skills/`.

### Windows PowerShell

```powershell
$target = Join-Path $HOME ".claude\skills"
New-Item -ItemType Directory -Force -Path $target | Out-Null
Copy-Item -Path ".\skills\*" -Destination $target -Recurse -Force
```

### Antigravity

لم يتم إثبات التوافق مع Antigravity في اختبار تثبيت فعلي حتى الآن. لا تعتبر تعليمات الاستيراد القديمة ضماناً للتوافق.

## سير العمل

1. استلام الطلب وإنشاء Creative Brief.
2. التحقق من Brand Contract عند استخدام هوية DigitalNawa.
3. تحليل Hook إذا احتاجت القصة إلى افتتاحية مخصصة.
4. إعداد Story Plan.
5. استخدام Cut Editor فقط عند وجود مواد خام تحتاج إلى قص.
6. إعداد Production Plan.
7. تنفيذ المعاينة عبر Remotion Engine.
8. فحص QC مع أدلة.
9. تنفيذ الرندر النهائي عند طلب التصدير صراحة.
10. إنشاء Delivery Manifest.

## التحقق من العقود

يتطلب Python 3.12 وبيئة التطوير:

```bash
python -m pip install -r requirements-dev.txt
python scripts/validate_contracts.py
```

## حدود الضمان

- JSON Schema يتحقق من بنية البيانات، ولا يثبت صحة محتواها أو حدوث التنفيذ.
- مهارات Claude لا توفر وحدها Runtime يفرض انتقالات المراحل آلياً.
- لا يُسمح بـ QC PASS دون دليل.
- لا تُعد الهوية معتمدة قبل التحقق من الأصول الرسمية.
- يجب التحقق من شروط ترخيص Remotion قبل الاستخدام التجاري أو الرندر المؤتمت.
- لا تُضمّن مفاتيح API أو أسراراً في المستودع.

## مصدر الحقيقة

المهارات النشطة موجودة في `skills/`. مجلدات المهارات المكررة في جذر المستودع إرث قديم ولن تُحذف ضمن هذه الخطوة؛ تزال فقط بعد خطة ترحيل واختبار توافق مستقلة.
