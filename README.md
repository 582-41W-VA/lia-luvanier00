![logo](wiobl/static/images/logo.png)
# West Island Outdoor Basketball League Website


## Table of Contents
1. [GitHub Repository](https://github.com/582-41W-VA/lia-luvanier00/tree/main)
2. [RFP (Request for Proposal)](https://docs.google.com/document/d/1WLQ_GswqJwIRbnHFPSIlzlHetLjbXj94HI-ERWHspRI/edit?tab=t.mpckphpi7ntj)
3. [Proposal](https://docs.google.com/document/d/1WLQ_GswqJwIRbnHFPSIlzlHetLjbXj94HI-ERWHspRI/edit?tab=t.9om3eiq4lxq)
4. [Entity Relationship Diagram](https://lucid.app/lucidchart/335aa6e0-9dd2-446b-80c1-2c08e38ef9b2/edit?beaconFlowId=1D63F15EC9B78776&invitationId=inv_94cee053-f71d-4cc7-9816-eb9320e8e7a1&page=0_0#)
5. [Figma Wireframes](https://www.figma.com/design/WLOc988dywSjxurEWN92fa/Wireframes?node-id=0-1&t=qbD3A2jEqaPXnfRB-1)
6. [Figma Visual Guidelines](https://www.figma.com/design/v0doO6UoSR8i3qQoqDcydy/Design-Guidelines?node-id=0-1&t=h61pWLCkiptjpuMn-1)


## Goal 

To create a website that acts as a central hub for WIOBL, making communication, registration, and league management easier for parents, players, and coaches.


## Our Team 

1. Luisa - Designer
2. Soula - Front-End Developer
3. Christen - Back-End Developer 
4. Molly - Repository Manager

## Instalation Steps

### 1. Clone the Repository

Run the following command in your terminal:
```
git clone https://github.com/582-41W-VA/lia-luvanier00.git
````
Navigate to the project directory:
```
cd project-repository
```

### 2. Install uv command to run script and manage python packages

- **Windows**
```
scoop install uv
```

- **Mac**
```
brew install uv
```

###  3. Set Up Python and Django

Ensure you have Python 3.8+ installed. Verify using:
```
python3 --version
```

### 4. Set up database

Apply database migrations:
```
uv run manage.py migrate
```


### 5. Run the Django Server
Start the development server:
```
uv run manage.py runserver
```
Open your browser and navigate to http://127.0.0.1:8000/ to view the application.

## Usage

### Admin Access

1. Access the admin dashboard at:
http://127.0.0.1:8000/admin

2. Default admin credentials:
- **Username** : admin
- **Password** : adminpassword

## Technologies used 

- **Back-end**: Django
- **Front-End**: HTML, CSS, Javascript
- **Database**: SQLite, Lucidchart (For ERD)
- **Design Tools**: Figma (Wireframes, Mockup and Design Guidelines)
- **API Integration**: Google Maps API (need to confirm)

## Contributing

To contribute:

1. **Clone the repository:**
```
git clone <repository-url>
```
```
cd <repository-name>
```

2. **Create a feature branch:**
```
git checkout -b feature-branch-name
```

3. **Make your changes**

4. **Add your changes to the staging area:**
*Stage all files*
```
git add .
```
*Stage specific file*
```
git add <filename>
```

5. **Commit your changes:**
```
git commit -m "Add feature"
```

6. **Push to the branch:**
```
git push origin feature-branch-name
```

7. **Review and approval:**
The repository manager will review your pull request, provide feedback if necessary, and approve it to be merged into the main branch.
