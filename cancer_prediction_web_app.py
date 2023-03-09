import streamlit as st
from streamlit_option_menu import option_menu





st.set_page_config(page_title="Cancer Prediction System", page_icon=":hospital:", layout="wide")


selected = option_menu(
            menu_title=None,  # required
            options=["Home", "Prediction"],  # required
            icons=["house","activity"],  # optional
            menu_icon="cast",  # optional
            default_index=0,  # optional
            orientation="horizontal",
        )
  
 
if selected == "Home":
            
            with st.container():
                    st.title("Overview")
                    st.write("Machine learning is a branch of artificial intelligence that employs a variety of statistical, probabilistic and optimization techniques that allows computers to “learn” from past examples and to detect hard-to-discern patterns from large, noisy or complex data sets. This capability is particularly well-suited to medical applications, especially those that depend on complex proteomic and genomic measurements. As a result, machine learning is frequently used in cancer diagnosis and detection. More recently machine learning has been applied to cancer prognosis and prediction. This latter approach is particularly interesting as it is part of a growing trend towards personalized, predictive medicine. In assembling this review we conducted a broad survey of the different types of machine learning methods being used, the types of data being integrated and the performance of these methods in cancer prediction and prognosis. A number of trends are noted, including a growing dependence on protein biomarkers and microarray data, a strong bias towards applications in prostate and breast cancer, and a heavy reliance on “older” technologies such artificial neural networks (ANNs) instead of more recently developed or more easily interpretable machine learning methods. A number of published studies also appear to lack an appropriate level of validation or testing. Among the better designed and validated studies it is clear that machine learning methods can be used to substantially (15–25%) improve the accuracy of predicting cancer susceptibility, recurrence and mortality. At a more fundamental level, it is also evident that machine learning is also helping to improve our basic understanding of cancer development and progression.")
            
            import streamlit as st
            from streamlit_option_menu import option_menu
            selected = option_menu(
                        menu_title=None,  # required
                        options=["Lung cancer", "Breast cancer", "Prostate cancer", "Contact"],  # required
                        menu_icon="cast",  # optional
                        default_index=0,  # optional
                        orientation="horizontal",
                    )
            
if selected == "Lung cancer":
          with st.container():
                  st.write("---")
                  left_column, right_column = st.columns(2)
          with left_column:
                  st.header("What is a Lung cancer?")
                  st.write("Cancer is a disease in which cells in the body grow out of control. When cancer starts in the lungs, it is called lung cancer.Lung cancer begins in the lungs and may spread to lymph nodes or other organs in the body, such as the brain. Cancer from other organs also may spread to the lungs. When cancer cells spread from one organ to another, they are called metastases.Lung cancers usually are grouped into two main types called small cell and non-small cell (including adenocarcinoma and squamous cell carcinoma). These types of lung cancer grow differently and are treated differently. Non-small cell lung cancer is more common than small cell lung cancer.")
                  st.write("Your lungs are 2 sponge-like organs in your chest. Your right lung has 3 sections, called lobes. Your left lung has 2 lobes. The left lung is smaller because the heart takes up more room on that side of the body.When you breathe in, air enters through your mouth or nose and goes into your lungs through the trachea (windpipe). The trachea divides into tubes called bronchi, which enter the lungs and divide into smaller bronchi. These divide to form smaller branches called bronchioles. At the end of the bronchioles are tiny air sacs known as alveoli.The alveoli absorb oxygen into your blood from the inhaled air and remove carbon dioxide from the blood when you exhale. Taking in oxygen and getting rid of carbon dioxide are your lungs’ main functions.Lung cancers typically start in the cells lining the bronchi and parts of the lung such as the bronchioles or alveoli.")
                  st.header("Types of lung cancer")
                  st.write("There are 2 main types of lung cancer and they are treated very differently.")
                  st.subheader("Non-small cell lung cancer (NSCLC)")
                  st.write("About 80% to 85% of lung cancers are NSCLC. The main subtypes of NSCLC are adenocarcinoma, squamous cell carcinoma, and large cell carcinoma. These subtypes, which start from different types of lung cells are grouped together as NSCLC because their treatment and prognoses (outlook) are often similar.Adenocarcinoma: Adenocarcinomas start in the cells that would normally secrete substances such as mucus.This type of lung cancer occurs mainly in people who currently smoke or formerly smoked, but it is also the most common type of lung cancer seen in people who don't smoke. It is more common in women than in men, and it is more likely to occur in younger people than other types of lung cancer.")
                  st.subheader("Small cell lung cancer (SCLC)")
                  st.write("About 10% to 15% of all lung cancers are SCLC and it is sometimes called oat cell cancer. This type of lung cancer tends to grow and spread faster than NSCLC. About 70% of people with SCLC will have cancer that has already spread at the time they are diagnosed. Since this cancer grows quickly, it tends to respond well to chemotherapy and radiation therapy. Unfortunately, for most people, the cancer will return at some point.")
                  st.header("Symptoms")
                  st.write("People with lung cancer may not have any symptoms until a later stage. If lung cancer signs do appear, they can resemble those of a respiratory infection.")
                  st.write("Some possible symptoms includeTrusted Source:changes to a person’s voice, such as hoarseness frequent chest infections, such as bronchitis or pneumonia,swelling in the lymph nodes in the middle of the chest, a lingering cough that may start to get worse, chest pain, shortness of breath and wheezing, In time, a person may also experience more severe symptoms, such as: severe chest pain,bone pain and bone fractures, headaches, coughing up blood, blood clots, appetite loss and weight loss,fatigue")
                    
          with right_column:
                  
                  from PIL import Image
                  st.image("https://www.cdc.gov/cancer/lung/images/lung-diagram-750.jpg?_=49525",width=(int(500)))
                  st.text(" ")
                  st.text(" ")
                  st.text(" ")
                  st.text(" ")
                  
                  st.image("https://my.clevelandclinic.org/-/scassets/images/org/health/articles/6202-small-cell-lung-cancer",width=(int(500)))
                  st.text(" ")
                  st.text(" ")
                  st.text(" ")
                  st.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT3r3R5yB6cCwoX3O9Nl-rg4x1jncbpBRhdJQ&usqp=CAU",width=(int(500)))
if selected == "Breast cancer":
                with st.container():
                  st.write("---")
                  left_column, right_column = st.columns(2)
                
                with left_column:
                        st.header("What is a Breast cancer?")
                        st.write("Breast cancer is cancer that forms in the cells of the breasts.After skin cancer, breast cancer is the most common cancer diagnosed in women in the United States. Breast cancer can occur in both men and women, but it's far more common in women.Substantial support for breast cancer awareness and research funding has helped created advances in the diagnosis and treatment of breast cancer. Breast cancer survival rates have increased, and the number of deaths associated with this disease is steadily declining, largely due to factors such as earlier detection, a new personalized approach to treatment and a better understanding of the disease.")
                        st.write("It’s important to understand that most breast lumps are benign and not cancer (malignant). Non-cancer breast tumors are abnormal growths, but they do not spread outside of the breast. They are not life threatening, but some types of benign breast lumps can increase a woman's risk of getting breast cancer. Any breast lump or change needs to be checked by a health care professional to find out if it is benign or malignant (cancer) and if it might affect your future cancer risk.")
                        st.header("Types of Breast Cancer")
                        st.write("types of breast cancer include ductal carcinoma in situ, invasive ductal carcinoma, inflammatory breast cancer, and metastatic breast cancer.")
                        st.subheader("Invasive breast cancer")
                        st.write("When breast cancer is called invasive (or infiltrating), it means it has spread into the surrounding breast tissue. The two most common types of invasive breast cancer are defined by where in the breast they begin to grow:")
                        st.write("Invasive ductal carcinoma (IDC) is invasive breast cancer that starts in the milk ducts, the tubes that carry milk from the lobules to the nipple. It is the most common type of breast cancer; about 80% of all breast cancers are invasive ductal carcinomas.")
                        st.write("Invasive lobular carcinoma (ILC) is invasive breast cancer that starts in the lobules, the glands in the breast that produce milk. It is the second most common type of breast cancer; about 10% of all invasive breast cancers are invasive lobular carcinomas.")    
                        st.subheader("Non-invasive breast cancer")
                        st.write("When breast cancer is called non-invasive (or in situ) it means it has not spread beyond the breast tissue where it started. Non-invasive breast cancers are also called precancers. There are two main types of non-invasive breast cancer:")
                        st.write("Ductal carcinoma in situ (DCIS), is non-invasive breast cancer that has not spread outside the milk ducts where it started. DCIS isn’t life threatening, but is considered a precursor to invasive breast cancer and increases the risk of developing an invasive breast cancer later in life. About 16% of all breast cancer diagnoses are DCIS.")
                        st.write("Lobular carcinoma in situ (LCIS), is non-invasive breast cancer that has not spread outside the lobules where it started. Despite its name, LCIS is a benign breast condition and is not a true breast cancer.")
                        st.subheader("Cancerous phyllodes tumors of the breast")
                        st.write("Phyllodes tumors of the breast are rare and make up fewer than 1% of all breast tumors. Most phyllodes tumors are benign (not cancerous), but about 25% are cancerous.")
                        st.header("What Are the Symptoms of Breast Cancer?")
                        st.write("Different people have different symptoms of breast cancer. Some people do not have any signs or symptoms at all.")
                        st.write("New lump in the breast or underarm (armpit),Thickening or swelling of part of the breast,Irritation or dimpling of breast skin,Redness or flaky skin in the nipple area or the breast,Pulling in of the nipple or pain in the nipple area,Nipple discharge other than breast milk, including blood,Any change in the size or the shape of the breast,Pain in any area of the breast.")
                with right_column:
                  from PIL import Image
                  st.image("https://d2jx2rerrg6sh3.cloudfront.net/image-handler/picture/2017/2/shutterstock_576066646.jpg",width=(int(500)))
                  st.text(" ")
                  st.text(" ")
                  st.text(" ")
                  st.text(" ")
                  
                  st.image("https://www.asbestos.com/wp-content/uploads/breast-cancer-diagram-1.png",width=(int(500)))
                  st.text(" ")
                  st.text(" ")
                  st.text(" ")
                  st.image("https://images.everydayhealth.com/images/types-of-breast-cancer-guide-1440x810.jpg?sfvrsn=974e3840_1",width=(int(500)))
                  st.text(" ")
                  st.text(" ")
                  st.text(" ")
                  st.image("https://lirp.cdn-website.com/69c0b277/dms3rep/multi/opt/Early+signs+-+symptoms+of+breast+cancer-640w.jpg",width=(int(500)))

            
if selected == "Prostate cancer":
                  with st.container(): 
                        st.write("---")
                        left_column, right_column = st.columns(2)

                  with left_column: 
                        st.header("What Is Prostate Cancer?")
                        st.write("Prostate cancer begins when cells in the prostate gland start to grow out of control. The prostate is a gland found only in males. It makes some of the fluid that is part of semen.The prostate is below the bladder (the hollow organ where urine is stored) and in front of the rectum (the last part of the intestines). Just behind the prostate are glands called seminal vesicles that make most of the fluid for semen. The urethra, which is the tube that carries urine and semen out of the body through the penis, goes through the center of the prostate.")
                        st.write("The size of the prostate can change as a man ages. In younger men, it is about the size of a walnut, but it can be much larger in older men.")
                        st.write("Prostate cancer is the most common type of cancer found in men in the United State, aside from skin cancer, and often begins without symptoms. Prostate cancer can be slow-growing, such that many men die of other diseases before the prostate cancer causes significant problems. However, many prostate cancers are more aggressive and can spread outside the confines of the prostate gland, which can be deadly. The prostate cancer survival rate is greatly improved with early detection and personalized treatment.")
                        st.header("Types of prostate cancer")
                        st.write("Almost all prostate cancers are adenocarcinomas. These cancers develop from the gland cells (the cells that make the prostate fluid that is added to the semen).")
                        st.write("Other types of cancer that can start in the prostate include: Small cell carcinomas,Neuroendocrine tumors (other than small cell carcinomas),Transitional cell carcinomas,Sarcomas")
                        st.write("These other types of prostate cancer are rare. If you are told you have prostate cancer, it is almost certain to be an adenocarcinoma.Some prostate cancers grow and spread quickly, but most grow slowly. In fact, autopsy studies show that many older men (and even some younger men) who died of other causes also had prostate cancer that never affected them during their lives. In many cases, neither they nor their doctors even knew they had it.")
                        st.subheader("Prostatic intraepithelial neoplasia (PIN)")
                        st.write("In PIN, there are changes in how the prostate gland cells look when seen with a microscope, but the abnormal cells don’t look like they are growing into other parts of the prostate (like cancer cells would). Based on how abnormal the patterns of cells look, they are classified as:")
                        st.write("Low-grade PIN: The patterns of prostate cells appear almost normal, High-grade PIN: The patterns of cells look more abnormal.")
                        st.write("Low-grade PIN is not thought to be related to a man’s risk of prostate cancer. On the other hand, high-grade PIN is thought to be a possible precursor to prostate cancer. If you have a prostate biopsy and high-grade PIN is found, there is a greater chance that you might develop prostate cancer over time.PIN begins to appear in the prostates of some men as early as in their 20s. But many men with PIN will never develop prostate cancer.")
                        st.subheader("Proliferative inflammatory atrophy (PIA)")
                        st.write("In PIA, the prostate cells look smaller than normal, and there are signs of inflammation in the area. PIA is not cancer, but researchers believe that PIA may sometimes lead to high-grade PIN, or perhaps directly to prostate cancer.")
                        st.header("What are the symptoms of Prostate cancer")
                        st.write("A symptom is something that only the person experiencing it can identify and describe, such as fatigue, nausea, or pain. A sign is something that other people can identify and measure, such as a fever, rash, or an elevated pulse. Together, signs and symptoms can help describe a medical problem. While most prostate cancer does not cause any symptoms at all, the symptoms and signs of prostate cancer may include:")
                        st.write("Frequent urination,Weak or interrupted urine flow or the need to strain to empty the bladder,The urge to urinate frequently at night,Blood in the urine,New onset of erectile dysfunction,Pain or burning during urination, which is much less common,Discomfort or pain when sitting, caused by an enlarged prostate")
                  with right_column:
                         
                        from PIL import Image
                        st.image("https://www.mayoclinic.org/-/media/kcms/gbs/patient-consumer/images/2013/11/15/17/38/ds00043_-my01633_im01561_prostca1thu_jpg.jpg",width=(int(500)))
                        st.text(" ")
                        st.text(" ")
                        st.text(" ")
                        st.text(" ")
                  
                        st.image("https://scch.co.in/Uploads/Cancer/CancerDetail/Service-cancer-desc-86527762.jpg",width=(int(500)))
                        st.text(" ")
                        st.text(" ")
                        st.text(" ")
                        st.image("https://actchealth.com/images/state-type.png",width=(int(500)))
                        st.text(" ")
                        st.text(" ")
                        st.text(" ")
                        st.image("https://medtalks.in/uploads/summnernote/summnernote-Cancer-in-english.jpeg",width=(int(500)))


if selected == "Contact":
                st.header(":mailbox: Get In Touch With Me!")
                
                
                contact_form = """
                <form action="https://formsubmit.co/naqeeb7506@gmail.com" method="POST">
                     <input type="hidden" name="_captcha" value="false">
                     <input type="text" name="name" placeholder="Your name" required>
                     <input type="email" name="email" placeholder="Your email" required>
                     <textarea name="message" placeholder="Your message here"></textarea>
                     <button type="submit">Send</button>
                </form>
                """
                
                st.markdown(contact_form, unsafe_allow_html=True)
                
                # Use Local CSS File
                def local_css(file_name):
                    with open(file_name) as f:
                        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
                
                
                local_css("D:\\Cancer Websites\\Cancer-prediction-using-machine-learning-main\\style.css")

if selected == "Prediction":
                    import pickle
                    import streamlit as st
                    from streamlit_option_menu import option_menu
                        
        
        
                    #loading the saved models
                    
                    prostate_cancer_model = pickle.load(open('/trained_model_prost.sav','rb'))
        
                    lung_cancer_model = pickle.load(open('D:\\Cancer Websites\\Cancer-prediction-using-machine-learning-main\\model_lung.sav','rb'))
        
                    breast_cancer_model = pickle.load(open('D:\\Cancer Websites\\Cancer-prediction-using-machine-learning-main\\breast_model.sav','rb'))
        
        
                    #sidebar for naviaget
        
        
                        
                    selected = option_menu( 'Cancer Prediction Systems',
                                               ['Prostate Cancer Prediction',
                                                'Lung Cancer Prediction',
                                                'Breast Cancer Prediction'],
                                               icons = ['x-octagon','activity','file-earmark-medical-fill'],
                                               default_index = 0,
                                               orientation="horizontal",
                                               styles={
                                                  "nav-link":{
                                                      "font-size":"15px",
                                                      "text-align":"left",
                                                      "margin":"0px",
                                                      "--hover-color":"#ff4b4b",
                                                      },
                                                  "container":{
                                                      "width":"100vw",
                                                      "padding":"0!important",
                                                      "background-color":"grey"}})
                        
                    if(selected == 'Prostate Cancer Prediction'):
                        
                        
                        #page title
                        st.title('Prostate Cancer Prediction using ML')
                    
                            
                        radius = st.text_input('radius')
                       
                        texture =st.text_input('texture')
                       
                        perimeter = st.text_input('perimeter')
                        area = st.text_input('area')
                        smoothness = st.text_input('smoothness')
                        #compactness = st.text_input('compactness')
                        #symmetry = st.text_input('symmetry')
                        #fractal_dimension = st.text_input('factal dimension')
                       
                        prostate_diagnosis = ''
    
                        if st.button('Predict'):
                            prostate_prediction = prostate_cancer_model.predict([[ radius,texture,perimeter,area,smoothness]])
         
                            if (prostate_prediction == 1):
                                
                                prostate_diagnosis = "the person have Prostate Cancer"
                            if(prostate_prediction == 0):
                                prostate_diagnosis = "the person is healthy"
                        st.success(prostate_diagnosis)
                      
                        
                    if(selected == 'Lung Cancer Prediction'):
                        
                        #page title
                        st.title('Lung Cancer Prediction System using ML')
                        
        
                        
                        Age=st.text_input('enter Your Age')
                        Smokes=st.text_input('Smoking level of the patient.')
                        AreaQ =st.text_input('Air Quality of the area where patient resides')
                        Alkhol =st.text_input('Alcohol Level Of the Patient')
                        
                        
                        
                        
                        lung_diagnosis = ''
                        
                        if st.button('Predict'):
                             lung_cancer_prediction =lung_cancer_model.predict([[Age,Smokes,AreaQ,Alkhol]])
                      
                             
                             if (lung_cancer_prediction  == 0):
                                 lung_diagnosis = "safe"
                             else:
                                lung_diagnosis = 'the person have lung Cancer'
                        st.success( lung_diagnosis)
                              
                             
                           
                      
                        
        
                    if(selected == 'Breast Cancer Prediction'):
                        
                        #page title
                        st.title('Breast Cancer Prediction System using ML')
                       
                       
        
        
                        
                        mean_radius = st.text_input('mean radius')
                        mean_texture = st.text_input('mean texture')
                        mean_perimeter = st.text_input('mean perimeter value')
                        mean_area = st.text_input('mean area')
                        mean_smoothness = st.text_input('mean smoothness')
                        mean_compactness = st.text_input('mean compactness')
                        mean_concavity = st.text_input('mean concavity')
                        mean_concave_points = st.text_input('mean concave')
                        mean_symmetry = st.text_input('mean symmetry')
                        mean_fractal_dimension = st.text_input('mean fractal dimension')
                        radius_error = st.text_input('radius error')
                        texture_error = st.text_input('texture error')
                        perimeter_error = st.text_input('perimeter error')
                        area_error = st.text_input('area error')
                        smoothness_error = st.text_input('smoothness error')
                        compactness_error = st.text_input('compactness error')
                        concavity_error = st.text_input('concavity error')
                        concave_points_error = st.text_input('concave points error')
                        symmetry_error = st.text_input('symmetry error')
                        fractal_dimension_error = st.text_input('fractal dimension error')
                        worst_radius = st.text_input('worst radius')
                        worst_texture = st.text_input('worst texture')
                        worst_perimeter = st.text_input('worst perimeter')
                        worst_area = st.text_input('worst area')
                        worst_smoothness = st.text_input('worst smoothness')
                        worst_compactness = st.text_input('worst compactness')
                        worst_concavity = st.text_input('worst concavity')
                        worst_concave_points = st.text_input('worst concave points')
                        worst_symmetry = st.text_input('worst symmetry')
                        worst_fractal_dimension = st.text_input('worst fractal dimension')
                        
                        
                        
                            
                        
                        breast_dignosis = ''
                        
                        
                        #creating a button for prediction
                        
                        if st.button('Predict'):
                             breast_prediction = breast_cancer_model.predict([[mean_radius,mean_texture,mean_perimeter,mean_area,mean_smoothness,mean_compactness,mean_concavity,mean_concave_points,mean_symmetry,mean_fractal_dimension,radius_error,texture_error,perimeter_error,area_error,smoothness_error,compactness_error,concavity_error,concave_points_error,symmetry_error,fractal_dimension_error,worst_radius,worst_texture,worst_perimeter,worst_area,worst_smoothness,worst_compactness,worst_concavity,worst_concave_points,worst_symmetry,worst_fractal_dimension]])
                             
                             if (breast_prediction == 0):
                                 breast_dignosis = "The Breast cancer is Malignant"
                             else:
                                breast_dignosis = 'The Breast Cancer is Benign'
                        st.success(breast_dignosis)
                      
                        

                        
                        
                        
                        
                        
                    
                    

