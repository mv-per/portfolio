function showTrackITDetails() {
    const modalContent = `
            <h4>TrackIT - Object Tracking Application</h4>
            <p><strong>Client Need:</strong> A comprehensive application to track objects in video with user management and simulation capabilities.</p>
            <div class="story-section">
                <h5>Key Features:</h5>
                <ul>
                    <li>Track objects in video using OpenCV</li>
                    <li>Complete user management system with SQL database</li>
                    <li>Backend API for video loading, simulation execution, and download</li>
                    <li>Frontend application with login, video management, and simulation controls</li>
                    <li>Customizable simulation options (line length, color, tracking algorithms)</li>
                    <li>Real-time progress tracking and video download functionality</li>
                </ul>
            </div>
            <div class="tech-stack">
                <strong>Backend:</strong> Python + FastAPI + SQLAlchemy + Alembic<br>
                <strong>Frontend:</strong> Angular2 + PrimeNG<br>
                <strong>Database:</strong> PostgreSQL (SQLAlchemy compatible)
            </div>
            <p><em>Full-stack solution delivering complete object tracking capabilities with professional user interface.</em></p>
        `;
    showModal(modalContent);
}

function showCheMLDetails() {
    const modalContent = `
            <h4>CheML - Chemical Engineering ML Toolkit</h4>
            <p><strong>Comprehensive Python toolkit for machine learning in Chemical Engineering</strong></p>
            <div class="story-section">
                <h5>Core Features:</h5>
                <ul>
                    <li><strong>ML Model Templates:</strong> Pre-built scikit-learn workflows</li>
                    <li><strong>Manufacturing Quality Prediction:</strong> FastAPI-based prediction endpoints</li>
                    <li><strong>MLflow Integration:</strong> Complete experiment tracking and model management</li>
                    <li><strong>Process Optimization:</strong> Advanced algorithms for chemical processes</li>
                    <li><strong>Real-time Predictions:</strong> Production endpoints with input validation</li>
                </ul>
            </div>
            <div class="story-section">
                <h5>Applications:</h5>
                <ul>
                    <li>Reaction yield forecasting</li>
                    <li>Quality control systems</li>
                    <li>Process optimization</li>
                    <li>Chemical property estimation</li>
                </ul>
            </div>
            <div class="tech-stack">
                <strong>Production Features:</strong> Conda environments, pre-commit hooks, comprehensive documentation, scalable architecture for industrial chemical engineering applications.
            </div>
        `;
    showModal(modalContent);
}

function showModal(content) {
    // Create overlay
    const overlay = document.createElement('div');
    overlay.style.position = 'fixed';
    overlay.style.top = '0';
    overlay.style.left = '0';
    overlay.style.width = '100%';
    overlay.style.height = '100%';
    overlay.style.backgroundColor = 'rgba(0, 0, 0, 0.5)';
    overlay.style.backdropFilter = 'blur(5px)';
    overlay.style.zIndex = '999';
    overlay.style.transition = 'opacity 0.3s ease';
    document.body.appendChild(overlay);

    // Create modal
    const modal = document.createElement('div');
    modal.style.position = 'fixed';
    modal.style.top = '50%';
    modal.style.left = '50%';
    modal.style.transform = 'translate(-50%, -50%)';
    modal.style.backgroundColor = 'white';
    modal.style.padding = '20px';
    modal.style.zIndex = '1000';
    modal.style.borderRadius = '8px';
    modal.style.boxShadow = '0 4px 8px rgba(0, 0, 0, 0.2)';
    modal.style.transition = 'transform 0.3s ease';
    modal.innerHTML = content;

    // Create close button
    const closeButton = document.createElement('button');
    closeButton.innerText = 'Close';
    closeButton.className = 'close-btn';
    closeButton.style.marginTop = '20px';
    closeButton.style.padding = '10px 20px';
    closeButton.style.backgroundColor = '#667eea';
    closeButton.style.color = 'white';
    closeButton.style.border = 'none';
    closeButton.style.borderRadius = '6px';
    closeButton.style.cursor = 'pointer';
    closeButton.style.fontSize = '1em';
    closeButton.style.fontWeight = '500';
    closeButton.style.transition = 'background-color 0.3s ease';
    closeButton.onmouseover = () => (closeButton.style.backgroundColor = '#764ba2');
    closeButton.onmouseout = () => (closeButton.style.backgroundColor = '#667eea');
    closeButton.onclick = () => {
        document.body.removeChild(modal);
        document.body.removeChild(overlay);
    };
    modal.appendChild(closeButton);

    // Append modal to the body
    document.body.appendChild(modal);
}