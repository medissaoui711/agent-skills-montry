# DigitalNawa Studio

مستودع Plugin لاستوديو إنتاج فيديو يعتمد مهارات متخصصة وعقود بيانات قابلة للتحقق، مع Remotion كمحرك الإنتاج الأساسي.

> **حالة الهوية:** قيم الألوان الأساسية الخمسة موثقة كقرارات معتمدة في DN-DEC-006. أما اعتماد الهوية الكاملة فما زال معلقاً بسبب عدم اعتماد الشعار النهائي والخطوط وملف الأصول النهائي.

## المكونات

- `montry`: تنسيق سير العمل وتحديد المهارات المطلوبة.
- `brand-digitalnawa`: التحقق من مصدر الهوية وإعداد Brand Contract.
- `hook-analyzer`: تحليل الافتتاحية عند الحاجة السردية.
- `cut-editor`: إعداد قرارات القص من المواد الخام.
- `motion-builder`: إعداد Production Plan.
- `remotion-engine`: معاينة وتنفيذ خطة الإنتاج باستخدام Remotion.
- `qc-checker`: فحص قائم على الأدلة.
- `contracts/`: سبعة JSON Schemas للعقود بين المراحل.
- `shared/brand/brand-contract.json`: سجل هوية قابل للتتبع؛ حالته الحالية PENDING وليست اعتماداً نهائياً للهوية.

## تثبيت Claude Code

### تشغيل المستودع كـ Plugin محلياً

من داخل مجلد المستودع نفسه:

```bash
claude --plugin-dir .
```

هذا أسلوب تطوير محلي؛ اتبع واجهة Plugin Manager في Claude Code للتثبيت الدائم.

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
python scripts/validate_plugin.py
python scripts/validate_workflow.py
python -m unittest discover -s tests -v
```

التحقق الأصلي من Plugin عبر Claude Code:

```bash
claude plugin validate . --strict
claude --plugin-dir . plugin details montry
```

اختبار التكامل يستخدم بيانات اصطناعية فقط. راجع [Integration Verification](docs/testing/integration-verification.md) وحالة بوابة Remotion قبل تشغيل أي معاينة فعلية.

## حدود الضمان

- JSON Schema يتحقق من بنية البيانات، ولا يثبت صحة محتواها أو حدوث التنفيذ.
- مهارات Claude لا توفر وحدها Runtime يفرض انتقالات المراحل آلياً.
- لا يُسمح بـ QC PASS دون دليل.
- الشعار النهائي والخطوط واعتماد حزمة الأصول ما زالت غير محسومة.
- يجب التحقق من شروط ترخيص Remotion قبل الاستخدام التجاري أو الرندر المؤتمت.
- لا تُضمّن مفاتيح API أو أسراراً في المستودع.

## مصدر الحقيقة

المهارات النشطة موجودة في `skills/`. مجلدات المهارات المكررة في جذر المستودع إرث قديم ولن تُحذف ضمن هذه الخطوة؛ تزال فقط بعد خطة ترحيل واختبار توافق مستقلة.

تفاصيل مصدر الهوية وحالة كل عنصر موثقة في [Brand Source Evidence](docs/brand/source-evidence.md).
