function dist(v, mu) {								
    const g = 9.81;
    const v_ms = v * 1000 / 3600; 
    const reaction_distance = v_ms * 1; 
    const braking_distance = (v_ms * v_ms) / (2 * mu * g);
    const total_stopping_distance = reaction_distance + braking_distance;
    return total_stopping_distance;
  }
  
  function speed(d, mu) {						
    const g = 9.81;
    const a = 1 / (2 * mu * g);
    const b = 1;
    const c = -d;
    const discriminant = b * b - 4 * a * c;
    const v_ms = (-b + Math.sqrt(discriminant)) / (2 * a);
    const v_kmh = v_ms * 3600 / 1000; 
    return v_kmh;
  }