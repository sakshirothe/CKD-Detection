def diagnose_health(age, bp, albumin, sugar, hemoglobin):
    """
    Performs a basic diagnosis based on a set of medical indicators.
    
    This is a simplified, rule-based system for demonstration purposes only and
    should not be used for actual medical diagnosis.
    
    Args:
        age (int): Patient's age.
        bp (int): Blood Pressure (systolic, e.g., 120).
        albumin (float): Albumin level in g/dL.
        sugar (float): Blood sugar level in mg/dL.
        hemoglobin (float): Hemoglobin level in g/dL.
        
    Returns:
        tuple: A message string with the diagnosis and a list of possible conditions.
    """

    possible_conditions = []
    
    # === CKD Detection Logic ===
    # This is a very simplified rule set to check for potential CKD
    # A real model would be far more complex. We count how many "red flags" are present.
    ckd_indicators = 0
    
    # A real model would use two values (systolic and diastolic) for blood pressure.
    # For this simplified model, we will assume we only have systolic blood pressure.
    if bp > 140:
        ckd_indicators += 1  # High BP is a major risk factor and symptom
    if albumin < 3.5:
        ckd_indicators += 1  # Low albumin can be a sign of protein loss
    if sugar > 125:
        ckd_indicators += 1  # High blood sugar (diabetes) is a leading cause
    if hemoglobin < 12.0:
        ckd_indicators += 1  # Anemia is common in advanced CKD
        
    if ckd_indicators >= 3:
        # If 3 or more indicators are present, we'll flag it as potential CKD.
        return "CKD Detected", ["Chronic Kidney Disease (CKD)"]
        
    # --- If CKD is not detected, check for other diseases that share symptoms ---
    
    # Anemia Check
    if hemoglobin < 12.0:
        possible_conditions.append("Anemia (Possible causes: iron deficiency, B12 deficiency, chronic disease)")
    
    # Hypertension Check
    if bp > 140:
        possible_conditions.append("Hypertension (High Blood Pressure)")
        
    # Hypoalbuminemia Check (if not CKD-related)
    if albumin < 3.5:
        possible_conditions.append("Hypoalbuminemia (Possible causes: liver disease, malnutrition)")

    # Diabetes Check
    if sugar > 125:
        possible_conditions.append("Diabetes Mellitus")

    if possible_conditions:
        # Return a list of other possible conditions if CKD is not the primary diagnosis.
        return "CKD Not Detected, but other conditions may exist:", possible_conditions
    else:
        # Return a clean bill of health if no indicators are present.
        return "No significant issues detected.", ["Normal Health Indicators"]

# --- Examples of how to use the function ---

# 1. Example with a high probability of CKD
# A 55-year-old with high BP, low albumin, very high sugar, and anemia.
ckd_diagnosis, ckd_conditions = diagnose_health(age=55, bp=160, albumin=2.5, sugar=220, hemoglobin=9.0)
print(f"--- CKD Example ---")
print(f"Diagnosis: {ckd_diagnosis}")
print(f"Possible Conditions: {ckd_conditions}")
print("-" * 20)

# 2. Example with no CKD, but other conditions
# A 55-year-old with high BP, low albumin, but normal sugar.
other_diagnosis, other_conditions = diagnose_health(age=55, bp=160, albumin=2.5, sugar=100, hemoglobin=9.0)
print(f"--- Other Conditions Example ---")
print(f"Diagnosis: {other_diagnosis}")
print(f"Possible Conditions: {other_conditions}")
print("-" * 20)

# 3. Example with a healthy individual
# A 55-year-old with normal indicators.
healthy_diagnosis, healthy_conditions = diagnose_health(age=55, bp=120, albumin=4.5, sugar=100, hemoglobin=14.5)
print(f"--- Healthy Example ---")
print(f"Diagnosis: {healthy_diagnosis}")
print(f"Possible Conditions: {healthy_conditions}")
print("-" * 20)
