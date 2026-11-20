# Cinemana Pro | المرجع الهندسي والبصري الشامل

**النسخة المرجعية:** Obsidian 04 / Liquid Glass V4  
**تاريخ التوثيق:** 18 نوفمبر 2026  
**الغرض:** ذاكرة عمل مستقلة وقابلة للاستعادة، توثق النسخ السابقة والنتائج والأدوات والمصادر وخطة بناء واجهة أفضل، وليس تعليمات لتعديل التطبيق الحالي تلقائياً.

> قاعدة المالك: التجارب هنا HTML/CSS/JS مستقلة. لا تعديل أو دفع commits إلى أي فرع في CP، ولا بناء APK، حتى يطلب المالك الدمج صراحةً. لا تستبدل واجهة التطبيق كلها مرة واحدة. أبقِ محرك التحميل الأصلي مستقلاً عن العرض.

## 1. السياق والهدف

- المشروع: [alwansan/CP](https://github.com/alwansan/CP)، فرع مرحلة التحميل [feature/download-stability](https://github.com/alwansan/CP/tree/feature/download-stability) للقراءة عند الحاجة فقط.
- الخطة التي قرئت في جلسة V1: [CP_HTML_HANDOFF_AR.md](https://github.com/alwansan/CP/blob/feature/download-stability/docs/CP_HTML_HANDOFF_AR.md)، [README](https://github.com/alwansan/CP/blob/feature/download-stability/README.md). وفق الخطة، baseline B1b3-12/h68 للتحميل، لا تعني مرحلة الإغلاق خلو المحرك من العيوب. لم تُراجع آخر HEAD في جلسة V4، ولا يُدّعى أن هذه الملفات بقيت بلا تغيير.
- المالك رفع `img.zip` وفيه 18 لقطة JPG من التطبيق الأصلي. استعملت النسخ V1–V4 قصاصات الصور المستخرجة في جلسة V1؛ الأصول موجودة داخل `assets/`، وليست مكتبة سينمانا الحية. لا تقدم بيانات التقييم والحلقات التجريبية على أنها حقائق محدثة.
- الهدف: واجهة عربية RTL، سينمائية، ملائمة للهاتف، ثلاث ثيمات (Dark/Light/OLED)، حركة سلسة، Liquid Glass متدرج الجودة، بحث واختيار حلقات وطابور تنزيلات وتحويل ومشغل وإعدادات وحساب محلي. الحفاظ على الوضوح والوصول إلى الوظائف بسرعة مع مئات عمليات التحميل.
- الجهاز المستهدف المعروف: POCO F5 Pro / Android 15 / Adreno 730 / شاشة 120Hz. لا توجد قياسات Android فعلية لهذه النسخة؛ يلزم اختبار WebView الحقيقي وليس محاكاة Chromium فقط.

## 2. تاريخ التجارب ومعرفة النسخ

| النسخة | إنجازها الأساسي | القيد |
|---|---|---|
| V1 | واجهات HTML تفاعلية مستقلة؛ صور المستخدم؛ تنقل وبحث ومشغل وتنزيلات محاكاة، 3 ثيمات | زجاج CSS أساسي، لا قياس هاتف |
| V2 | Glass Lab، Eco/Balanced/Prism، ألوان، كثافة، تباين، حفظ تجريبي، تحديث تقدم دون إعادة بناء الصفحة | انعكاس بصري CSS، تخزين مختبر shim |
| V3 | تصميم cinema-first، إكمال المشاهدة، عدسة WebGL/Canvas | Canvas اختبر فعلاً، WebGL لم يعمل في بيئة الاختبار؛ الشريط CSS فقط |
| V4 | Obsidian 04، زجاج منشوري SVG خلف شريط حي، بحث عربي مطبع وسجل محلي، طابور 24 صفاً/صفحة واختبار 480 عنصر إضافي | SVG مثبت في Chromium لا في Android، WebGL غير مثبت، تخزين origin الحقيقي محظور |

هذه خلاصة مبنية على مراجعة ملفات V3 ولقطات V3 وقراءة الكود وإعادة اختبار V4. حافظ على V1–V3 كمرجع ومقارنة؛ لا تحذفها. ملفات V4 المستقلة: `Cinemana-Liquid-Glass-V4.html`؛ `Cinemana-Liquid-Glass-V4-Source.zip`؛ `Cinemana-Liquid-V4-Preview.jpg`؛ هذا المرجع.

## 3. نقد V3 والقرارات في V4

| الملاحظة | قرار V4 | السبب / حدود القرار |
|---|---|---|
| كثرة الزجاج بالأزرار والقوائم | أسطح محتوى أهدأ، زجاج بالطبقة العائمة والأزرار المهمة | هرم بصري أقوى ولا ضبابية على الصور |
| ازدحام مقدمة الرئيسية | نقل التصنيفات بعد صورة العرض؛ عنوان «اكتشف عالمك» | تحسين التسلسل البصري؛ اختيار تصميمي قابل للتغيير |
| الضبابية ليست انكساراً | SVG displacement map لحافة dock في Prism؛ Canvas/WebGL في المختبر | لا ادعاء محاكاة فيزيائية كاملة |
| كل صفوف الطابور ترسم دفعةً واحدة | pagination بحجم 24، فلترة وحالة وبحث | حد عقد DOM المعروضة؛ ليس virtual scrolling كاملاً |
| `find` لكل صف أثناء تحديث النسب | Map من keys وتحديث الصفوف المعروضة | تقليل البحث المتكرر؛ ما زال إنشاء Map وفحص القائمة كلفة خطية |
| تبديل البحث يغير اتجاه المستخدم | سجل بحث حتى 6، تطبيع التشكيل والألف والياء، إبقاء حقل بحث الطابور عند استبدال النتائج | تجربة أفضل، لا fuzzy search كاملة |
| القوائم تحتاج إغلاق واضح | شريط إغلاق لكل dialog وaria-labelledby | قابلية الاستخدام، لم يُختبر قارئ شاشة فعلي |
| عرض حالة «قيد التحميل» للمنتظر | فصل انتظار/متوقف/قيد المحاكاة/مكتمل | نموذج فقط، لا نقل لبروتوكول native |

## 4. نظام التصميم Obsidian 04

- Canvas `#090A0D`؛ Surface `#17191E`؛ Text `#F8F4EE`؛ Muted `#B5B7C1`؛ Coral `#FF786F`. زر العرض العاجي `#F7F3EC` / `#141416`. الوضع الفاتح والأسود والألوان الثلاثة محفوظة من V3.
- الخط الحالي Tahoma/Arial أو النظام؛ لا خطوط الإنترنت ولا مكتبات خارجية لتشغيل نموذج HTML. مستقبلاً جرّب IBM Plex Sans Arabic / Tajawal / Cairo حسب ترخيص الخط، حجم الملف والتشكيل. لا تفرض الخط قبل مقارنة القراءة على الجهاز.
- قياس المسافات 4/8/12/16/20/24، أهداف لمس رئيسية >=44px (ليست دعوى أن كل مساحة تحقق المعيار)، زوايا البطاقات 13–26px وشريط 34px. استخدم `padding-inline` و`margin-inline` حيث يمكن، لا تثبت right/left لمكونات قابلة للعكس إلا بسبب هندسي مبرر.
- Glass modes: Eco صلب، Balanced ضبابية 13px تقريبياً، Prism تأثير `url(#dock-lens) blur(4px)` مع خريطة normals PNG مضمنة؛ `CSS.supports` يختبر قبول الصيغة لا ضمان عملها بصرياً. وضع التباين العالي/إيقاف الزجاج يتجاوز الانكسار. لا تبديل تلقائي بناء على استهلاك فعلي بعد.
- الحركة: transition بين الصفحات ~380ms؛ dock ~440ms spring-like؛ hero zoom 1 ثانية محدود؛ pointer reflection حدثي بـrequestAnimationFrame؛ احترام toggle الحركة و`prefers-reduced-motion`. لا حلقة صوت أو تحريك مستمر للزجاج. بعض تحديثات progress/layout تبقى بحاجة profiling.
- المعاينة البصرية لها صورتان للـdock فوق خطوط اختبار: `dock-optical.png` و`dock-blur.png`. الفرق المرصود دليل على تغيير بكسلات، وليس إثبات أن انكسار الحواف يحاكي كل خصائص الزجاج الحقيقي.

## 5. الفهرس الوظيفي في V4

| صفحة | السلوك الحالي |
|---|---|
| الرئيسية | عروض 3، سحب وتحديد العرض، فتح التفاصيل، إضافات للمفضلة والطابور، إكمال مشاهدة تجريبي |
| الأقسام | تصنيفات وبطاقات أفلام ومسلسلات وأنمي وقائمة المفضلة |
| البحث | تطبيع عربي، فلاتر سنة/نوع/تقييم، سجل بحث يدوياً قابل للمسح |
| التفاصيل | موسم وحلقات، اختيار متعدد وحفظ، معاينة مشغل |
| التحميلات | إيقاف/استئناف/حذف، تبويبان، بحث، فلتر انتظار/متوقف، 24 صفاً لكل صفحة |
| مختبر الضغط | يضيف 480 مفتاحاً وهمياً دون تنزيل ملفات؛ إعادة الضغط لا يكرر نفس المفاتيح؛ حذف `stress-*` فقط |
| الحساب | اسم محلي تجريبي، قائمة للمشاهدة لاحقاً، إعدادات |
| الإعدادات | لون/ثيم/كثافة/حركة/تباين/زجاج، إعداد تنزيلات تجريبي، ترجمة ومشغل معاينة |
| مختبر الزجاج | WebGL attempt / Canvas / Eco؛ يدعم touch/pointer؛ لا رندر دائم |

محاكاة التحميل ليست backend. اختيار حد التحميلات هو حد محاكاة فقط. بعض إعدادات المستخدم والإجراءات هي نماذج تصميم وليست وظائف أصلية كاملة. لا يوجد بث أو تسجيل دخول فعلي أو رابط signed URL أو FFmpeg.

## 6. سجل الأدوات والإضافات وMCP (تمييز الاستخدام الحقيقي)

### أ. الأدوات التي نُفذت فعلياً في هذه الجلسة V4

| الأداة | الاستخدام / الدليل |
|---|---|
| Shell / Python | قراءة النسخ الحالية وفتح اللقطات، نسخ مشروع مستقل، توليد خريطة normals PNG، جمع HTML، حساب فرق بكسلات وإعداد المعاينات |
| Node.js 22.16.0 | `node --check` للتحقق من بناء JS نحوياً؛ ليس Android runtime |
| Chromium + Playwright (Python library، ليس MCP) | لقطات شاشة فعلية، اختبارات التفاعل والضغط والتخطيط والفلتر بصرياً؛ وضع offline |
| Pillow | توليد displacement map وقياس الفرق وتجميع contact sheet |
| Web search | بحث المراجع الرسمية أدناه: Apple، MDN، web.dev، Chrome، Android، WCAG، MCP |
| Context7 MCP (Upstash) | `resolve_library_id` لـ MDN و`query_docs` بالمعرف `/mdn/content`: دلالة backdrop root ودعم SVG URL filters، دون إرسال كود المشروع |
| Superpowers (skill) | قراءة verification-before-completion وتطبيق التحقق قبل الادعاءات. لم تُشغّل شبكة subagents |
| HyperFrames (skill + مصدر) | قراءة قواعد HTML والـGSAP timeline؛ تحديث تركيبة V4 ولقطات الشاشة؛ لا تشغيل CLI أو تصدير MP4 فعلي في V4 |
| HTML/CSS/JS/WAAPI/SVG | الواجهة المستقلة والمكونات والحركات والفلاتر؛ Canvas 2D وWebGL shader تجريبي من V3 |

### ب. أدوات المراحل السابقة / المتصلة لكن لم تنفذ في V4

- **GitHub MCP**: قرأ ملفات handoff وREADME من الفرع في V1. لم يقرأ/يكتب المستودع في V4. المشروع التجريبي لا يعتمد على GitHub كي يعمل.
- **Website Design**: تمت قراءة مهارات design-direction/design-review/page-design في نقاش الإضافات السابق؛ أفكار نظام التصميم والاستجابة والتباين. لم يُنشأ موقع مستضاف أو build link.
- **Product Design (OpenAI)**: اتصال مؤكد؛ مهارات index/get-context قرئت في V3. لم يتم إنشاء prototype خارجي أو استدعاء image generation في V4. لعمل workflow الكامل استخدم البيئة التي تدعمه.
- **Figma**: اتصال مؤكد؛ صالح لإنتاج design tokens ومكونات قابلة للتحرير ومقارنة الشاشات. لم يتم إنشاء أو تعديل ملف Figma في V3/V4؛ لا تدّع ذلك.
- **MagicPath**: اتصال مؤكد؛ مناسب للمفاهيم البديلة والاختبار التفاعلي على canvas. لم يتم إرسال صور المستخدم أو إنشاء مشروع خارجي في V4. لا ترفع الأصول الخاصة إلى طرف ثالث دون تحقق من الإذن.
- **Context7** و**Superpowers**: اتصال مؤكد كما فوق؛ الحالة ليست ضماناً لاستخدام كل إمكانيات الأداة. راجع وجودها في الجلسة الجديدة قبل التنفيذ.
- **HyperFrames**: مثبت/متوفر منذ V1. CLI تعذر في المحاولات السابقة بسبب الوصول إلى npm. لا تصف HTML التطبيق على أنه فيديو HyperFrames. التركيبة المنفصلة تستخدم `gsap@3.14.2` عبر CDN وتحتاج إتاحة المكتبة عند التصيير، أما التطبيق فلا يحتاجها.

### ج. أدوات MCP إضافية بحثت عنها (مقترحة، غير مثبتة/غير مؤكدة داخل ChatGPT)

| الأولوية | الأداة الرسمية | الاستخدام والقرار |
|---|---|---|
| P0 | [Chrome DevTools MCP](https://github.com/ChromeDevTools/chrome-devtools-mcp) | trace للـJS/layout/paint, console, heap، GPU حيث تتوفر القياسات؛ الأفضل للتحقق من تكلفة الزجاج. يتطلب متصفح متاح وعميل MCP يدعم تشغيله. لا يثبت FPS Android دون جهاز |
| P0 | [Playwright MCP](https://github.com/microsoft/playwright-mcp) · [docs](https://playwright.dev/docs/getting-started-mcp) | تفاعل ولقطات وaccessibility snapshots؛ يسهّل الاختبارات. مكتبة Playwright الحالية تؤدي أغلب المطلوب؛ MCP اختياري وليس شرطاً |
| P1 | [Google Stitch](https://stitch.withgoogle.com/) · [stitch-skills](https://github.com/google-labs-code/stitch-skills) | مفاهيم واجهات وأنظمة تصميم عبر MCP، مفيد للمقارنة؛ لا تعتمد الإخراج بلا مراجعة أو اختبار، تحقق من شروط الخدمة والاتصال |
| P1 | [Penpot MCP](https://help.penpot.dev/mcp/) · [المصدر](https://github.com/penpot/penpot-mcp) | بديل مفتوح لـFigma، قراءة وكتابة التصميم، مفيد للـSVG والتوكنز؛ لا حاجة لتكرار الأداتين إذا كان Figma يكفي |
| P2 | [shadcn/ui MCP](https://ui.shadcn.com/docs/mcp) | استكشاف registries لمكونات حديثة، لا تنقل React/Tailwind تلقائياً إلى WebView؛ اقتبس الأفكار أو نفذ Vanilla بحسب الحاجة والترخيص |

**طريقة الاختيار:** لا تحتاج تثبيت كل الأدوات. أبدأ بـDevTools + Playwright للقياس ثم Stitch أو Penpot إذا احتجنا اتجاهات جديدة، وshadcn عند البحث عن مكوّن محدد. هذه خوادم خارجية تتطلب بيئة تدعم MCP. لم أتأكد من وجودها في دليل ChatGPT أو عملها على خطة المالك/الهاتف. لا تمنحها وصول GitHub أو جلسة متصفح خاصة إذا لا يلزم ذلك. روابط المستودعات موثقة أعلاه لا تعليمات تثبيت غير مختبرة.

## 7. مراجع البحث وتصميم Liquid Glass

### المصادر التي قدمها المالك

هذه قائمة مراجع المستخدم للرجوع إليها؛ بعضها مرجع ملهم/تجريبي وليس معياراً. لا يدّعي V4 زيارة جميع الروابط أو استيراد مكونات Figma منها. استخدمنا المبدأ العام والمراجع الرسمية المتاحة، لا نقل مباشر للواجهات.

- [Figma Liquid Glass UI plugin](https://www.figma.com/community/plugin/1514769156504171663/liquid-glass-ui)
- [LiquidGlassDesign](https://liquidglassdesign.com/) · [Liqui](https://liqui.design/)
- [Motion The Agency — Apple Liquid Glass](https://www.motiontheagency.com/blog/apple-liquid-glass-design)
- [Apple Newsroom — new software design](https://www.apple.com/newsroom/2025/06/apple-introduces-a-delightful-and-elegant-new-software-design/)
- [Dribbble Liquid Glass](https://dribbble.com/search/liquid-glass)
- [UI Layouts Liquid Glass](https://www.ui-layouts.com/components/liquid-glass)
- [Setproduct practical guide](https://www.setproduct.com/blog/liquid-glass-design-explained-a-practical-guide)
- [Figma iOS 26 Liquid Glass kit](https://www.figma.com/community/file/1532382036345480633/apple-ios-26-liquid-glass-by-junii-designs)

### مصادر V4 التي بحثت فيها فعلياً

| المصدر | المبدأ الذي أخذناه / الاستفادة |
|---|---|
| [Apple — Materials](https://developer.apple.com/design/human-interface-guidelines/materials) | طبقة وظيفية عائمة مستقلة عن المحتوى، تحكم بالتباين والشفافية |
| [Apple — Adopting Liquid Glass](https://developer.apple.com/documentation/TechnologyOverviews/adopting-liquid-glass) | تأثر الزجاج بالمحتوى والتفضيلات؛ تخصيص بحذر |
| [WWDC25 — Meet Liquid Glass](https://developer.apple.com/videos/play/wwdc2025/219/) | تقليل زجاج فوق زجاج، المحافظة على التباين |
| [WWDC25 — new design system](https://developer.apple.com/videos/play/wwdc2025/356/) | الانفصال عن المحتوى والتدرجات المدروسة |
| [Apple — Color](https://developer.apple.com/design/human-interface-guidelines/color) | ضرورة القراءة فوق خلفية متعددة الألوان |
| [MDN — backdrop-filter](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/backdrop-filter) | SVG URL filter، backdrop root؛ راجعنا أيضاً Context7 `/mdn/content` |
| [MDN SVG filters](https://developer.mozilla.org/en-US/docs/Web/SVG/Guides/Filters) | `feDisplacementMap` لإزاحة البكسلات؛ لا يساوي ray tracing |
| [MDN View Transition API](https://developer.mozilla.org/en-US/docs/Web/API/View_Transition_API) | اتجاه مستقبلي لانتقالات مشتركة بين ملصق وتفاصيل، ليس مستخدماً في V4 |
| [web.dev — animations guide](https://web.dev/articles/animations-guide) | تحريك transform/opacity قدر الإمكان، قياس كلفة الخصائص الأخرى |
| [web.dev — long tasks](https://web.dev/articles/optimize-long-tasks) | منع المهام الطويلة على main thread، تقسيم الأعمال أو نقلها إلى Worker عند الحاجة |
| [Chrome — performance](https://developer.chrome.com/docs/modern-web-guidance/guides/performance/performance) | تقليل حجم DOM وتأجيل الرسم تحت الطية؛ لا تطبيق content-visibility المكلف على عناصر البداية |
| [WCAG 2.2](https://www.w3.org/TR/WCAG22/) | تباين 4.5:1 للنص العادي، 3:1 للنص الكبير وعناصر التحكم ذات الصلة، التركيز، الأهداف، الوصول؛ يلزم تدقيق مستقل لكل ثيم |
| [GSAP docs](https://gsap.com/docs/v3/GSAP/) | timelines للعرض، ليست مكتبة مطلوبة لتشغيل تطبيق V4 |
| [Android — local content](https://developer.android.com/develop/ui/views/layout/webapps/load-local-content) | WebViewAssetLoader وHTTPS virtual local origin للمستقبل |
| [Android — native bridge](https://developer.android.com/develop/ui/views/layout/webapps/native-api-access-jsbridge) | `addWebMessageListener` مع allowed origins، اكتشاف AndroidX WebKit feature |
| [Android — insecure bridges](https://developer.android.com/privacy-and-security/risks/insecure-webview-native-bridges) | منع bridge واسع لأصل غير موثوق |
| [OWASP — origin scoped messaging](https://mas.owasp.org/MASTG/best-practices/MASTG-BEST-0035/) | تفضيل رسائل محددة الأصل على legacy bridge |

### مكتبات إضافية للتطوير (ليست كلها MCP)

- [Rive](https://rive.app/) للمكونات المتجهية التفاعلية وstate machines عند الحاجة. [Lottie](https://airbnb.io/lottie/) للأنيميشنات المتجهية المعدّة مسبقاً. استخدمهما انتقائياً للـempty states أو مؤشرات مميزة؛ راجع الترخيص، حجم runtime والتكلفة لكل فريم.
- [GSAP](https://gsap.com/) و[Motion](https://motion.dev/) للتسلسل والحركات المركبة؛ لا تلزم للمؤثرات البسيطة والتي تعمل بـCSS/WAAPI. [Lucide](https://lucide.dev/) أو [Tabler](https://tabler.io/icons) لنظام أيقونات واحد متجانس، لا خلط عشوائي. راجع تراخيص المكونات قبل توزيعها.
- [Magic UI](https://magicui.design/) و[shadcn/ui](https://ui.shadcn.com/) و[UI Layouts](https://www.ui-layouts.com/) مراجع مكونية، لا تنقل إلى الإنتاج مباشرة دون قياس ومراجعة وصول وترخيص.
- Canvas / WebGL / WebGL2 لاستكشاف مواد shader على مساحة صغيرة؛ WebGPU لا يُعتمد إلا بعد تحقق من Android WebView ودعم الجهاز. لا تنتقل إليه لمجرد حداثته.

## 8. التحليل التقني لزجاج V4

1. خريطة RGB PNG بحجم 512×100، R/G مشتقان من اتجاه normal تقريبي لكبسولة SDF قرب الحد، القيم المتعادلة 128، B=128. ضُمّنت data:image/png في `feImage` وتغذي `feDisplacementMap`.
2. في Prism يحاول CSS تطبيق `backdrop-filter: url(#dock-lens) blur(4px) saturate(155%) brightness(.78)` للداكن، مع ضبط الفاتح. هذه إزاحة للصورة المأخوذة من backdrop الحقيقي وليست `filter` مطبقة على نصوص dock.
3. لا يوجد التقاط شاشة مستمر أو CPU readback للـDOM في الشريط. المتصفح مسؤول عن تركيب الفلتر؛ تكلفة GPU/CPU غير مقاسة على Android.
4. مختبر V3 الموروث يستخدم texture مرسومة، WebGL shader إن نجح، أو Canvas2D يقرأ العينات ويغير مواضع القنوات ويضيف لمعاناً. اختبار تغيّر البكسلات في Canvas مثبت. `CPOptics.dispose()` عند إغلاق المختبر يوقف RAF والمستمعين. WebGL لا يزال مساراً غير مثبت.
5. الفرق البصري ليس قياس دقة فيزيائية: اختبرنا شريطاً فوق خلفية خطوط متكررة مع تثبيت blur/tint، وقارنا نفس الحجم. تغيرت 24,942 بكسل من 111,744 عند عتبة RGB max>8 في إحدى التشغيلات. هذا يثبت أثراً بصرياً في هذا Chromium فقط. أعداد المقارنة قد تختلف حسب GPU/إصدار المتصفح.

### خطة Optics V5

- اختبر خريطة متجاوبة مع عرض وحجم الـdock، Fresnel رقيق وحواف ذات مستويات؛ لا ترسم فوق النصوص. قارن قبل/بعد على خلفيات صور فاتحة وداكنة ونصوص متحركة.
- Feature flags لكل تأثير: clear / tinted / Eco؛ fallback عند فقدان السياق أو ظهور flicker أو تشوه؛ فكر بقياس بسيط عند بدء التشغيل مع اختيار يدوي دائماً.
- اختبار A/B في WebView على الهاتف لزمن الإطار والحرارة وRSS/PSS. هدف 60Hz <=16.67ms أو 120Hz <=8.33ms نظرياً؛ ليس وعداً بتحقيقه. قارن p50/p95/p99 والإطارات المتعثرة ومدة الضغط.
- لا تستخدم مؤثرات blur على صفحات تنزيل مزدحمة، ولا `will-change` على كل عنصر؛ حدد الميزانية قبل زيادة الشفافية. استعمل صور WebP محلية عند ضمان توافقها وفحص الجودة.

## 9. هندسة التطبيق عند الدمج (تصور، لم يُنفذ)

وفق ملف handoff: المحرك Native يملك DB، حالات التنزيل، طابور العمل الدائم، Android service، MKV وFFmpeg. الواجهة HTML تعرض snapshot وتبعث أفعالاً معرّفة فقط. لا تضع DB أو الشبكة أو FFmpeg على main thread، ولا تضف محرك تحميل ثانياً. لا تعتمد localStorage لبيانات عمليات الإنتاج.

```text
Android Native download engine / DB / workers
       ↓ snapshot (revision) + bounded delta events
 origin-scoped WebMessage bridge + validation + ACK
       ↓
 presentation state store -> page selectors -> bounded DOM
       ↑ command: requestId, action, validated IDs
 native durable ACK -> reconcile -> state update
```

- `WebViewAssetLoader` على origin محلي موثوق مثل `https://appassets.androidplatform.net/assets/www/index.html`. حدّد allowlist بدقة في `WebViewCompat.addWebMessageListener` مع `WebViewFeature.isFeatureSupported(...)`. لا تجعل نافذة تعرض موقعاً خارجياً تحمل نفس الصلاحيات.
- رسائل versioned، requestId فريد، عملية idempotent، TTL/limits، ACK بعد الحفظ الدائم، sequence/revision، deltas مجمعة، replay أو reconcile عند فقد الرسائل، إعادة snapshot عند ربط WebView. جميع المعرفات تُحقق native؛ لا raw tokens ولا ملفات حساسة أو signed URLs داخل HTML.
- CSP في نسخة الإنتاج (self assets، لا scripts من الشبكة)، لا `allowUniversalAccessFromFileURLs`، حظر arbitrary navigation/iframe، allowlist intents. النموذج standalone inline ليس CSP للإنتاج. افحص مصادر HTML المتغيرة؛ `escapeText` للمدخلات المحلية؛ استكمل validation لجميع snapshots قبل native integration.
- اختبار الضغط: addBatch 400+ يحدث TX/ACK واحدة أو دفعات مقيدة، تدفق updates 10–30Hz? ابدأ بتجميع 100–250ms للـdeltas ثم قس؛ تقدم العرض المرئي يمكن interpolation خفيف. لا تربط سرعة المحرك بمدة animation. لا تعد بتحميل ملفات دون native اختبار.
- اجعل تغييرات الصفحات مستقلة عن العمل؛ احتفظ بـscroll/search/filter states؛ عند kill/rotate/reload تأكد من عدم فقدان الطابور أو التكرار. تحقق من restart mid-MKV، مساحة التخزين، انقطاع الشبكة، SQLite busy وrace pause/delete/cancel. راجع شروط h68/recovery الفعلية، لا تستبدلها من الذاكرة.
- دمج تدريجي: feature flag لشاشة واحدة، fallback native، مقارنة لقطات وحالات واختبارات ART/API35 والتوقيع، ثم تجارب الهاتف. لا تغيير فرع أو بناء إلا بإذن صريح من المالك.

## 10. اختبارات V4 وسجل الأدلة

- التحقق النحوي `node --check app.js` و`node --check optics.js` مطلوبة.
- `test_ui.py`: مسار الرئيسية/بحث/تفاصيل/تحميل متعدد/طابور/تبديل مظهر/إيقاف الزجاج/تنقل؛ لقطات 8 شاشات، بلا page errors في المسار المختبر.
- `test_v2.py`: regression للتحكم بالزجاج واللون والكثافة، حفظ shim، تقدم محاكاة أثناء التنقل وعدم تبدل نفس DOM node عند tick، إيقاف الكل وتصفية/رجوع من البحث وguard للتحميل المتعدد.
- `test_v3.py`: Canvas refraction response، Eco، Prism، motion toggle، استعادة shim، hero counter، معاينة إكمال المشاهدة، 20 تركيبة عرض/صفحة (320/360/412/768 × 5 صفحات) دون overflow أفقي.
- `test_v4.py`: تطبيع Arabic search، البحث السابق ومسحه، 480 synthetic + 3 baseline = 483، 362 غير مكتمل و121 مكتمل، DOM حد 24 صفاً، pagination 16 صفحة في active، filter متوقف، البحث داخل الطابور يحتفظ بالتركيز، التحقق من تحديث DOM دون إعادة رسم، حذف عناصر stress فقط، Prism/Eco، صفر uncaught JS errors في المسارات المختبرة. `test-results-v4.json` أعداد بكسلات ووقت desktop headless في التشغيل؛ ليس FPS أو benchmark هاتف. لا تخلط click→assert مع زمن إرسال native.
- تجربة `test_storage_v4.py` الأصل الحقيقي عبر route اصطناعي offline **تعذرت** `ERR_BLOCKED_BY_ADMINISTRATOR`. الاختبارات السابقة استخدمت storage shim. لا يدّعي V4 إثبات localStorage عبر إعادة تشغيل المتصفح الحقيقي؛ التخزين يحتاج تحقق على الهاتف.
- اختبارات إضافية قبل الإنتاج: 400/1000/5000 entries، 30min/60min soak، إيقاف واستئناف وتعليق الواجهة، RTL landscape، keyboard/IME، system back، rotation، screen reader TalkBack، contrast لكل artwork، text scale 200%، airplane mode، power saver؛ اختبار V4 لا يثبت هذه الحالات.

## 11. أولويات V5–V6 (خطة وليست إنجازاً)

| الأولوية | البند | معيار الاعتماد |
|---|---|---|
| P0 | اختبار V4 على الهاتف واختيار الوضع الأفضل | لا تقطيع مزعج، نص مقروء، لا قص بالأزرار، قارن Prism/Balanced/Eco |
| P0 | profiling على WebView الفعلي | traces ومقارنة frame times + memory + حرارة أثناء الضغط؛ لا ادعاءات دون logs |
| P0 | Native bridge contract مستقل وآمن | mock snapshot/delta/reconcile، أمثلة negative tests، no secret leakage |
| P1 | إعادة هندسة الملفات إلى modules قابلة للاختبار | فصل catalog, router, store, simulator, glass, screen components؛ لا تضف framework إلا إذا كان له مبرر |
| P1 | تحسين التنقل وBack stack + route state | تفاصيل → رجوع يحفظ موضع القائمة والبحث، system back، modal stack، اختبارات متكررة |
| P1 | تنزيلات production-grade | تجميع حسب المسلسل/الموسم، bulk select، priority/retry/error state، أزرار إيقاف مؤقت/إلغاء مع تأكيد عند حذف ملف حقيقي |
| P1 | تصميم الأيقونات والحركة | اختبار Rive/Lottie محدود وCSS View Transitions progressive enhancement، reduced motion |
| P1 | تعميم التوكنز في Figma (اختياري) | ملف منفصل قابل للتحرير؛ tokens + variants لجميع الثيمات؛ لا رفع لقطات خاصة بلا إذن |
| P2 | بحث أسرع وفلاتر مركبة | debounce/IME/fuzzy/index، تستمد بياناتها من native أو cache موثوق، لا نتائج وهمية في الإنتاج |
| P2 | مشغل حقيقي وملخص مشاهدة | عقد تشغيل native واضح، ترجمة حقيقية وجودات وسجل مشاهدة لا تفقده إعادة إنشاء الصفحة |
| P2 | فيديو استعراض HyperFrames | lint/validate/inspect + render حقيقي 1080p؛ منفصل عن UI runtime |

## 12. التشغيل واستعادة جلسة جديدة

- على الهاتف افتح standalone HTML من Downloads بمتصفح يدعم JS. جرّب Prism، Balanced، Eco. ملحوظة: المتصفح المدمج قد يعطل JS/التخزين أو `backdrop-filter`؛ افتح في Chromium/متصفح حديث خارجي إذا تعذر.
- على جهاز/CI يتوفر فيه Python + chromium + Playwright + Pillow: فك ZIP، نفّذ `python build.py`، ثم `node --check app.js`، `node --check optics.js` واختبارات `test_ui.py`, `test_v2.py`, `test_v3.py`, `test_v4.py`. اختبار التخزين الحقيقي منفصل وقابل لإعادة التجربة عند توفر بيئة أصلية. يمكن تعديل مسار Chromium حسب البيئة. لا تشغل هذه الاختبارات كجزء من تنزيلات production.

### رسالة استعادة قابلة للنسخ

> تابع Cinemana Pro UI من V4 / Obsidian 04. اقرأ `CINEMANA_UI_MASTER_AR.md` و`DESIGN.md` و`README_AR.md` و`test-results-v4.json` والكود واللقطات من ZIP. فرع CP المرجعي feature/download-stability للقراءة فقط. ممنوع تعديل أي فرع أو APK دون توجيهي. هدفنا واجهات HTML/CSS/JS عربية محلية، Liquid Glass متعدد الجودة، أداء عملي مع مئات التحميلات. V4 يستخدم SVG displacement للشريط في Prism وCanvas في المختبر، WebGL غير مثبت على بيئة الاختبار. استمر بتجارب مستقلة وملفات V5/V6، وثق البحث والأدوات التي استعملتها فعلاً وما لم تستعمله، وغيّر سجل النتائج فقط بعد تحقق. قبل الدمج قِس على POCO F5 Pro، احفظ محرك التحميل الأصلي وعقد native الآمن. لا تدّع اختبار Android أو حفظ حقيقي إذا لم يثبت. انتهِ بملف HTML مستقل + source ZIP + معاينة + تحديث MD.

## 13. القيود والقرارات غير المعتمدة من المالك

اسم Obsidian 04، ارتفاع الـhero، وضع الفلتر المنشوري فقط، 24 صفاً لكل صفحة، حد 6 أبحاث سابقة، وعدد 480 عنصراً تجريبياً كلها قرارات تصميم/هندسة اتخذتها في هذه التجربة لتسهيل القياس؛ قابلة للتغيير. لا يوجد دليل أن هذه القرارات هي المثلى على الهاتف. لا تغييرات على المستودع. لا تصريف MP4. لا WebGL موثوق في البيئة، لا أصل localStorage حقيقي محقق، لا قياس FPS/PSS/حرارة أو تطبيق WCAG شامل. لا استضافة خارجية ولا ملف Figma/MagicPath خارجي جديد. كل ملفات الصور للمعاينة مبنية على النموذج الحالي، وليست ادعاء استعادة مكتبة التطبيق الحية.
