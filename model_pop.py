# model_pop.py

# import os
import csumuriaopt as ada
import numpy as np


def model_pop(wl, pop_opt_dir, pop_name_list=None, ret=False):
    #   Create parameterized aerosol populations with optical and hygroscopicity parameters for model aerosol populations
    spam = ada.OptAnalysis(pop_opt_dir=pop_opt_dir)
    recalc_pop_opt = True
    if pop_name_list is None:
        pop_name_list = []
        all_pop = True
    else:
        all_pop = False

    # --- WRF-CHEM ---
    # - Sea-Salt 1 -
    # TODO: convert from effective radius to equivalent bin or distribution
    name = 'WRF_SEAS_1'
    modes = 1                       # Number of modes in distribution
    mu = 171.                       # Median diameter (nm)
    gsd = 2.03                       # Geometric standard deviation
    mf = 1.0                        # Modal number fraction
    kappa = 0.8                     # Modal kappa hygroscopicity parameter
    dry_m = np.complex(1.495,1.0e-8)  # Modal complex index of refraction
    dens = 2.2                      # Density
    # - Setup variables -
    # parameters for each mode are sent as arrays in the form:
    parms = np.array([mu,gsd,mf])
    # kappa and refractive index variables to be used by hygroscopicity and mie classes
    var = {'kappa':kappa, 'dry_m':dry_m, 'density':dens}
    # - Crete a new aerosol population using the cn_dist() method -
    if name in pop_name_list or all_pop:
        spam.pop_opt(name=name,
                 wl=wl, ovr=recalc_pop_opt,
                 num_parm=parms, modes=modes,
                 auto_bins=True, nbins=100,
                 var=var)

    # - Sea-Salt 2 -
    # TODO: convert from effective radius to equivalent bin or distribution
    name = 'WRF_SEAS_2'
    modes = 1                       # Number of modes in distribution
    mu = 571.                       # Median diameter (nm)
    gsd = 2.03                       # Geometric standard deviation
    mf = 1.0                        # Modal number fraction
    kappa = 0.8                     # Modal kappa hygroscopicity parameter
    dry_m = np.complex(1.495,1.0e-8)  # Modal complex index of refraction
    dens = 2.2                      # Density
    # - Setup variables -
    # parameters for each mode are sent as arrays in the form:
    parms = np.array([mu,gsd,mf])
    # kappa and refractive index variables to be used by hygroscopicity and mie classes
    var = {'kappa':kappa, 'dry_m':dry_m, 'density':dens}
    # - Crete a new aerosol population called 'pop1' using the cn_dist() method -
    if name in pop_name_list or all_pop:
        spam.pop_opt(name=name,
                 wl=wl, ovr=recalc_pop_opt,
                 num_parm=parms, modes=modes,
                 auto_bins=True, nbins=100,
                 var=var)

    # - Sea-Salt 3 -
    # TODO: convert from effective radius to equivalent bin or distribution
    name = 'WRF_SEAS_3'
    modes = 1                       # Number of modes in distribution
    mu = 1856.                       # Median diameter (nm)
    gsd = 2.03                       # Geometric standard deviation
    mf = 1.0                        # Modal number fraction
    kappa = 0.8                     # Modal kappa hygroscopicity parameter
    dry_m = np.complex(1.495,1.0e-8)  # Modal complex index of refraction
    dens = 2.2                      # Density
    # - Setup variables -
    # parameters for each mode are sent as arrays in the form:
    parms = np.array([mu,gsd,mf])
    # kappa and refractive index variables to be used by hygroscopicity and mie classes
    var = {'kappa':kappa, 'dry_m':dry_m, 'density':dens}
    # - Crete a new aerosol population called 'pop1' using the cn_dist() method -
    if name in pop_name_list or all_pop:
        spam.pop_opt(name=name,
                 wl=wl, ovr=recalc_pop_opt,
                 num_parm=parms, modes=modes,
                 auto_bins=True, nbins=100,
                 var=var)

    # - Sea-Salt 4 -
    # TODO: convert from effective radius to equivalent bin or distribution
    name = 'WRF_SEAS_4'
    modes = 1                       # Number of modes in distribution
    mu = 4283.                       # Median diameter (nm)
    gsd = 2.03                       # Geometric standard deviation
    mf = 1.0                        # Modal number fraction
    kappa = 0.8                     # Modal kappa hygroscopicity parameter
    dry_m = np.complex(1.495,1.0e-8)  # Modal complex index of refraction
    dens = 2.2                      # Density
    # - Setup variables -
    # parameters for each mode are sent as arrays in the form:
    parms = np.array([mu,gsd,mf])
    # kappa and refractive index variables to be used by hygroscopicity and mie classes
    var = {'kappa':kappa, 'dry_m':dry_m, 'density':dens}
    # - Crete a new aerosol population called 'pop1' using the cn_dist() method -
    if name in pop_name_list or all_pop:
        spam.pop_opt(name=name,
                 wl=wl, ovr=recalc_pop_opt,
                 num_parm=parms, modes=modes,
                 auto_bins=True, nbins=100,
                 var=var)


    # --- RAMS ---
    # - Sea-Salt film mode-
    # TODO: convert from effective radius to equivalent bin or distribution
    name = 'RAMS_salt_film'
    modes = 1                       # Number of modes in distribution
    mu = 200.                       # Median diameter (nm)
    gsd = 1.80                      # Geometric standard deviation
    mf = 1.0                        # Modal number fraction
    kappa = 0.80                    # Modal kappa hygroscopicity parameter
    dry_m = np.complex(1.50,1.0E-8)  # Modal complex index of refraction
    dens = 2.2                      # Density
    # - Setup variables -
    # parameters for each mode are sent as arrays in the form:
    parms = np.array([mu,gsd,mf])
    # kappa and refractive index variables to be used by hygroscopicity and mie classes
    var = {'kappa':kappa, 'dry_m':dry_m, 'density':dens}
    # - Crete a new aerosol population called 'pop1' using the cn_dist() method -
    if name in pop_name_list or all_pop:
        spam.pop_opt(name=name,
                 wl=wl, ovr=recalc_pop_opt,
                 num_parm=parms, modes=modes,
                 auto_bins=True, nbins=100,
                 var=var)

    # - Sea-Salt jet mode -
    # TODO: convert from effective radius to equivalent bin or distribution
    name = 'RAMS_salt_jet'
    modes = 1                       # Number of modes in distribution
    mu = 2000.                      # Median diameter (nm)
    gsd = 1.80                      # Geometric standard deviation
    mf = 1.0                        # Modal number fraction
    kappa = 0.80                    # Modal kappa hygroscopicity parameter
    dry_m = np.complex(1.50,1.0E-8)  # Modal complex index of refraction
    dens = 2.2                      # Density
    # - Setup variables -
    # parameters for each mode are sent as arrays in the form:
    parms = np.array([mu,gsd,mf])
    # kappa and refractive index variables to be used by hygroscopicity and mie classes
    var = {'kappa':kappa, 'dry_m':dry_m, 'density':dens}
    # - Crete a new aerosol population called 'pop1' using the cn_dist() method -
    if name in pop_name_list or all_pop:
        spam.pop_opt(name=name,
                 wl=wl, ovr=recalc_pop_opt,
                 num_parm=parms, modes=modes,
                 auto_bins=True, nbins=100,
                 var=var)

    # - Sea-Salt spume mode -
    # TODO: convert from effective radius to equivalent bin or distribution
    name = 'RAMS_salt_spume'
    modes = 1                       # Number of modes in distribution
    mu = 12000.                     # Median diameter (nm)
    gsd = 1.80                      # Geometric standard deviation
    mf = 1.0                        # Modal number fraction
    kappa = 0.80                    # Modal kappa hygroscopicity parameter
    dry_m = np.complex(1.50,1.0E-8)  # Modal complex index of refraction
    dens = 2.2                      # Density
    # - Setup variables -
    # parameters for each mode are sent as arrays in the form:
    parms = np.array([mu,gsd,mf])
    # kappa and refractive index variables to be used by hygroscopicity and mie classes
    var = {'kappa':kappa, 'dry_m':dry_m, 'density':dens}
    # - Crete a new aerosol population called 'pop1' using the cn_dist() method -
    if name in pop_name_list or all_pop:
        spam.pop_opt(name=name,
                 wl=wl, ovr=recalc_pop_opt,
                 num_parm=parms, modes=modes,
                 auto_bins=True, nbins=100,
                 var=var)

    # - Dust1 mode -
    # TODO: convert from effective radius to equivalent bin or distribution
    name = 'RAMS_dust1'
    modes = 1                       # Number of modes in distribution
    mu = 1398.                     # Median diameter (nm)
    gsd = 1.80                      # Geometric standard deviation
    mf = 1.0                        # Modal number fraction
    kappa = 0.04                    # Modal kappa hygroscopicity parameter
    dry_m = np.complex(1.50,0.005)  # Modal complex index of refraction
    dens = 2.5                      # Density
    # - Setup variables -
    # parameters for each mode are sent as arrays in the form:
    parms = np.array([mu,gsd,mf])
    # kappa and refractive index variables to be used by hygroscopicity and mie classes
    var = {'kappa':kappa, 'dry_m':dry_m, 'density':dens}
    # - Crete a new aerosol population called 'pop1' using the cn_dist() method -
    if name in pop_name_list or all_pop:
        spam.pop_opt(name=name,
                 wl=wl, ovr=recalc_pop_opt,
                 num_parm=parms, modes=modes,
                 auto_bins=True, nbins=100,
                 var=var)

    # - Dust2 mode -
    # TODO: convert from effective radius to equivalent bin or distribution
    name = 'RAMS_dust2'
    modes = 1                       # Number of modes in distribution
    mu = 5900.                     # Median diameter (nm)
    gsd = 1.80                      # Geometric standard deviation
    mf = 1.0                        # Modal number fraction
    kappa = 0.05                    # Modal kappa hygroscopicity parameter
    dry_m = np.complex(1.50,0.005)  # Modal complex index of refraction
    dens = 2.65                      # Density
    # - Setup variables -
    # parameters for each mode are sent as arrays in the form:
    parms = np.array([mu,gsd,mf])
    # kappa and refractive index variables to be used by hygroscopicity and mie classes
    var = {'kappa':kappa, 'dry_m':dry_m, 'density':dens}
    # - Crete a new aerosol population called 'pop1' using the cn_dist() method -
    if name in pop_name_list or all_pop:
        spam.pop_opt(name=name,
                 wl=wl, ovr=recalc_pop_opt,
                 num_parm=parms, modes=modes,
                 auto_bins=True, nbins=100,
                 var=var)

    # - ccn mode -
    # TODO: convert from effective radius to equivalent bin or distribution
    name = 'RAMS_ccn'
    modes = 1                       # Number of modes in distribution
    mu = 80.                     # Median diameter (nm)
    gsd = 1.80                      # Geometric standard deviation
    mf = 1.0                        # Modal number fraction
    kappa = 0.55                    # Modal kappa hygroscopicity parameter
    dry_m = np.complex(1.524,1e-7)  # Modal complex index of refraction
    dens = 1.76                      # Density
    # - Setup variables -
    # parameters for each mode are sent as arrays in the form:
    parms = np.array([mu,gsd,mf])
    # kappa and refractive index variables to be used by hygroscopicity and mie classes
    var = {'kappa':kappa, 'dry_m':dry_m, 'density':dens}
    # - Crete a new aerosol population called 'pop1' using the cn_dist() method -
    if name in pop_name_list or all_pop:
        spam.pop_opt(name=name,
                 wl=wl, ovr=recalc_pop_opt,
                 num_parm=parms, modes=modes,
                 auto_bins=True, nbins=100,
                 var=var)

    # - regen_aero1 mode -
    # TODO: convert from effective radius to equivalent bin or distribution
    name = 'RAMS_regen_aero1'
    modes = 1                       # Number of modes in distribution
    mu = 20.                     # Median diameter (nm)
    gsd = 1.80                      # Geometric standard deviation
    mf = 1.0                        # Modal number fraction
    kappa = 0.17                    # Modal kappa hygroscopicity parameter
    dry_m = np.complex(1.524,6e-3)  # Modal complex index of refraction
    dens = 2.4                      # Density
    # - Setup variables -
    # parameters for each mode are sent as arrays in the form:
    parms = np.array([mu,gsd,mf])
    # kappa and refractive index variables to be used by hygroscopicity and mie classes
    var = {'kappa':kappa, 'dry_m':dry_m, 'density':dens}
    # - Crete a new aerosol population called 'pop1' using the cn_dist() method -
    if name in pop_name_list or all_pop:
        spam.pop_opt(name=name,
                 wl=wl, ovr=recalc_pop_opt,
                 num_parm=parms, modes=modes,
                 auto_bins=True, nbins=100,
                 var=var)

    # - regen_aero2 mode -
    # TODO: convert from effective radius to equivalent bin or distribution
    name = 'RAMS_regen_aero2'
    modes = 1                       # Number of modes in distribution
    mu = 2000.                     # Median diameter (nm)
    gsd = 1.80                      # Geometric standard deviation
    mf = 1.0                        # Modal number fraction
    kappa = 0.17                    # Modal kappa hygroscopicity parameter
    dry_m = np.complex(1.524,6e-3)  # Modal complex index of refraction
    dens = 2.4                      # Density
    # - Setup variables -
    # parameters for each mode are sent as arrays in the form:
    parms = np.array([mu,gsd,mf])
    # kappa and refractive index variables to be used by hygroscopicity and mie classes
    var = {'kappa':kappa, 'dry_m':dry_m, 'density':dens}
    # - Crete a new aerosol population called 'pop1' using the cn_dist() method -
    if name in pop_name_list or all_pop:
        spam.pop_opt(name=name,
                 wl=wl, ovr=recalc_pop_opt,
                 num_parm=parms, modes=modes,
                 auto_bins=True, nbins=100,
                 var=var)

    if ret:
        return spam
