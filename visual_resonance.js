// visual_resonance.js

function drawResonance(canvasId, strengthS3, strengthTi) {
    const canvas = document.getElementById(canvasId);
    const ctx = canvas.getContext('2d');
    const width = canvas.width;
    const height = canvas.height;
    
    ctx.clearRect(0, 0, width, height);
    
    const centerX = width / 2;
    const centerY = height / 2;
    
    // Draw S3 (Earth) node
    ctx.beginPath();
    ctx.arc(centerX - 100, centerY, 30, 0, 2 * Math.PI);
    ctx.fillStyle = `rgba(0, 150, 255, ${strengthS3})`;
    ctx.fill();
    ctx.fillStyle = 'white';
    ctx.fillText('S3', centerX - 100, centerY);
    
    // Draw Ti (Humanity) node
    ctx.beginPath();
    ctx.arc(centerX + 100, centerY, 30, 0, 2 * Math.PI);
    ctx.fillStyle = `rgba(255, 100, 0, ${strengthTi})`;
    ctx.fill();
    ctx.fillStyle = 'white';
    ctx.fillText('Ti', centerX + 100, centerY);

    // Draw the resonating bridge
    const gradient = ctx.createLinearGradient(centerX - 100, centerY, centerX + 100, centerY);
    const resonance = (strengthS3 + strengthTi) / 2;
    
    gradient.addColorStop(0, `rgba(0, 255, 255, ${resonance})`);
    gradient.addColorStop(0.5, `rgba(255, 255, 0, ${resonance})`);
    gradient.addColorStop(1, `rgba(0, 255, 255, ${resonance})`);
    
    ctx.beginPath();
    ctx.moveTo(centerX - 70, centerY);
    ctx.lineTo(centerX + 70, centerY);
    ctx.lineWidth = 5 * resonance; // Resonance strength affects line thickness
    ctx.strokeStyle = gradient;
    ctx.stroke();

    ctx.fillStyle = 'lime';
    ctx.font = '16px Arial';
    ctx.textAlign = 'center';
    ctx.fillText(`Resonance Strength: ${resonance.toFixed(2)}`, centerX, centerY + 50);
}

// Example usage
// Simulate different resonance states
// You can use these values to visualize real-time resonance
drawResonance('myCanvas', 0.8, 0.7); 
