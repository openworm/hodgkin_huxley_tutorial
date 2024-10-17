## Jupyter notebook for the Hodgkin Huxley model

This is an interactive web notebook using [Jupyter technologies](https://jupyter.org/) which can be used to run the HH model, change the parameters of the model and display the dynamical properties of variables.

<p align="center" ><kbd><a href="#running-the-notebook"><img src="../../Tutorial/_media/HH_Jupyter.png" width="600"/></a></kbd></p>

This notebook was developed as part of [Google Summer of Code 2022 by Rahul Sonkar](notebooks/GSoC_2022_Submission/GSoC_Documentation.md).

## Running the notebook

### Option 1) Using Open Source Brain version 2

*Advantage: you can save any changes you make to the notebook in your [OSBv2 workspace](https://docs.opensourcebrain.org/OSBv2/Overview.html), and view/edit other files associated with the model including the [Python implementation of the HH model](https://github.com/openworm/hodgkin_huxley_tutorial/blob/master/Tutorial/Source/HodgkinHuxley.py).*

- Go to [Open Source Brain v2](https://v2.opensourcebrain.org) and [register for a new account](https://docs.opensourcebrain.org/OSBv2/Guided_tour.html#register-sign-in-to-osbv2) and log in.
- Go to the Hodgkin Huxley model repository page at https://v2.opensourcebrain.org/repositories/33.
- Click on **New workspace from selection** (blue button).
- When this has been created, go to the new workspace page and click on **Open with JupyterLab**.
- This opens a copy of all the files in the repository in [JupyterLab](https://docs.opensourcebrain.org/OSBv2/JupyterLab.html#osbv2-applications-jupyterlab).
- In the left had file browser navigate to the folder `Hodgkin Huxley Tutorials/master/notebooks/Python_HH_version` and double click on `Python_Notebook_HH.ipynb` to open the notebook.
- You should be able to run the interactive widget by click the double arrow (&#9654;&#9654;) in the JupyterLab toolbar at the top of the notebook.
- Note: the lighter version of the JupyterLab interface shown above can be accessed in the menu: `Settings -> Theme -> JupyterLab Light`.


### Option 2) Using Binder

*Advantage: quick to start & run, no login required*

- The notebook can also be opened using [Binder](https://mybinder.org/). Click here to open the HH notebook: [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/openworm/hodgkin_huxley_tutorial/master?labpath=notebooks%2FPython_HH_version%2FPython_Notebook_HH.ipynb)-
- You should be able to run the interactive widget by click the double arrow (▶▶) in the JupyterLab toolbar at the top of the notebook.

### Option 3) Using Google Collab

*Advantage: can store your progress on your Google drive, but requires Google account and additional setup*

- The notebook can also be opened in [Google Collab](https://colab.research.google.com/github/openworm/hodgkin_huxley_tutorial/blob/master/notebooks/Python_HH_version/Python_Notebook_HH.ipynb), but you will need to add a new cell to the top of the notebook and paste the following to set it up to run properly:


    from google.colab import output
    output.enable_custom_widget_manager()

    from google.colab import drive
    drive.mount("/content/gdrive")

    %cd /content/gdrive/MyDrive
    !ls
    !rm -rf hodgkin_huxley_tutorial  # remove this line if you do not want to remove your existing copy to create a new one
    !git clone --depth 1 https://github.com/openworm/hodgkin_huxley_tutorial/
    %cd hodgkin_huxley_tutorial/
    !pip install -r requirements.txt
    %cd notebooks/Python_HH_version/


This does the following:

- asks you to allow Google Collab access your Google Drive when run for the first time: please allow all permissions
- mounts your Google Drive
- copies the GitHub repositoriy into it under the "hodgkin_huxley_tutorial" folder
- installs the required Python packages
